set :application, "AssistantPro, LLC"
set :repository,  "git@bitbucket.org:amadison/www.assistantproiowa.com.git"

set :scm, :git

ssh_options[:keys] = [File.join(ENV["HOME"], "ec2", "amadison-west.pem")]
role :web, "ec2-50-112-52-176.us-west-2.compute.amazonaws.com"                          # Your HTTP server, Apache/etc
role :app, "ec2-50-112-52-176.us-west-2.compute.amazonaws.com"
#role :db,  "your primary db-server here", :primary => true # This is where Rails migrations will run
#role :db,  "your slave db-server here"

set :website_host, 'www.assistantproiowa.com'
set :virtualenv_name, 'python-env'
set :settings_file, 'prod_settings'

set :deploy_to, "/var/www/#{website_host}"
set :user, "ec2-user"
set :use_sudo, false


after 'deploy:update_code', :prepare_virtualenv
after :prepare_virtualenv, :prepare_django
after :prepare_django, :upload_vhost
after 'deploy:symlink', :restart_apache


# override to remove some Rails specific stuff
namespace :deploy do  
    task :finalize_update, :except => { :no_release => true } do
        run "chmod -R g+w #{latest_release}" if fetch(:group_writable, true)
    end
end

def run_in_virtualenv(command)
    run "cd #{current_release} &&
    source #{virtualenv_name}/bin/activate &&
    #{command}"
end

def django_manage(manage_command)
    run_in_virtualenv("python src/manage.py #{manage_command} --noinput --settings=#{settings_file}")
end

desc "Makes virtual environment and installs projects requirements file." 
namespace :prepare_virtualenv do
    
    task :default do
        create_virtualenv
        install_dependencies
    end
    
    task :create_virtualenv do
        run "cd #{current_release} &&
             virtualenv #{virtualenv_name}"
    end
    
    task :install_dependencies do
        run_in_virtualenv("pip install -r requirements.txt")
    end
    
end

desc "collects static, syncdb and migrates database"
namespace :prepare_django do
    task :default do
        django_manage("collectstatic")
        django_manage("syncdb")
        #django_manage("migrate")
    end
end


desc "Generates vhost file and uploads to servers."
task :upload_vhost do
    require 'erb'
        
    template = ERB.new(File.read('config/templates/vhost.erb'), nil, '<>')
    result = template.result(binding)
    
    put(result, "/etc/httpd/sites-enabled/#{website_host}")
end
    

desc "Restarts apache"
task :restart_apache do
    run "sudo httpd -k graceful"
end

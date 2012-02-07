
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from web import views

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="web/index.html"), name='home'),
    url(r'^services/$', TemplateView.as_view(template_name="web/services.html"), name='services'),
    url(r'^rates/$', TemplateView.as_view(template_name="web/rates.html"), name='rates'),
    # url(r'^src/', include('src.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

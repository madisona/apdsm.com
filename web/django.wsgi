import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
project_dir = os.path.join(parent_dir, 'src')

for path in [parent_dir, project_dir]:
    if path not in sys.path:
        sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'src.prod_settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
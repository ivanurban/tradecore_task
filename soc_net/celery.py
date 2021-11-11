from __future__ import absolute_import
import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soc_net.settings')

#createj an instance of the application with app = Celery(''
app = Celery('soc_net')

##load any custom configuration from your project settings using the config_from_object()
app.config_from_object('django.conf:settings', namespace='CELERY')


# telling Celery to auto-discover asynchronous tasks for applications. 
# Celery will look for a tasks.py file in each application
# directory of applications added to INSTALLED_APPS in order to load
# asynchronous tasks defined in it
app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))
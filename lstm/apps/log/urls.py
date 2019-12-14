#------------------------------------------------------------------------------
# LSTM UI Django Project
# By japoveda10
# urls.py
# This file configures the app's urls
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Imports
#------------------------------------------------------------------------------
from django.urls import path, include
from .views import index, about, contact_us, test, get_data
from . import views
from rest_framework import routers

#------------------------------------------------------------------------------
# Router
#------------------------------------------------------------------------------
router = routers.DefaultRouter()
router.register('eventlogs', views.EventLogViewSet)
router.register('runningcases', views.RunningCaseViewSet)

#------------------------------------------------------------------------------
# URL Patterns
#------------------------------------------------------------------------------
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact_us/', contact_us, name='contact_us'),
    path('test/', test, name='test'),
    path('api/', include(router.urls)),
    path('results/', get_data, name="results"),
]
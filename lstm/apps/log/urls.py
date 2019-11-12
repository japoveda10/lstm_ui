from django.urls import path, include
from .views import index, about, contact_us, get_data
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('eventlogs', views.EventLogViewSet)
router.register('runningcases', views.RunningCaseViewSet)

# Wires up API using automatic URL routing
# Login URLs are included for browsable API
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact_us/', contact_us, name='contact_us'),
    path('api/', include(router.urls)),
    path('results/', get_data, name="results"),
]
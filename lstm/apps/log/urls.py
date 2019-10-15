from django.urls import path, include
from .views import index, about, contact_us, get_data, predict
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('eventlogs', views.EventLogView)

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact_us/', contact_us, name='contact_us'),
    path('predict/', predict, name='Show Results'),
    path('api/', include(router.urls)),
    path('results/', get_data, name="results")
]
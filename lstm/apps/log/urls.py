from django.urls import path  
from .views import index, step1

urlpatterns = [
    path('', index, name='log'),
    path('step1/', step1, name='step1')
]
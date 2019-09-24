from django.urls import path  
from .views import index, step1, about, contact_us

urlpatterns = [
    path('', index, name='home'),
    path('step1/', step1, name='step1'),
    path('step1/post', index, name='home'),
    path('about/', about, name='about'),
    path('contact_us/', contact_us, name='contact_us'),
]
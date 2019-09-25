from django.urls import path  
from .views import index, about, contact_us

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact_us/', contact_us, name='contact_us'),
]
from django.urls import path

from .views import register, profile, update_profile


urlpatterns = [
        path('', register, name='register'),
        path('profile', profile, name='profile'), 
        path('update_profile', update_profile, name='update_profile'),
]

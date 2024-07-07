from django.urls import path
from .views import create_api_key, shorten

urlpatterns = [
    path('create_api_key', create_api_key),
    path('shorten', shorten)
]
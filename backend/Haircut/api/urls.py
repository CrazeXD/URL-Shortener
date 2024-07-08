from django.urls import path
from .views import shorten

urlpatterns = [
    path('shorten', shorten)
]
from django.urls import path
from .views import site_view

urlpatterns = [
    path('', site_view, name='site'),
    path('<str:alias>/', site_view, name='site')
]

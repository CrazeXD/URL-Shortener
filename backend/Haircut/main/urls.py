from django.urls import path
from .views import site_view, registration_api_view

urlpatterns = [
    path('', site_view, name='site'),
    path('signup/', registration_api_view, name='signup'),
    path('<str:alias>/', site_view, name='site')
]

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.site),
    path('signup/', views.signup),
    path('login/', views.login),
]
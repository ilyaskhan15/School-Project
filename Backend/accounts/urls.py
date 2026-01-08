# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('users/', views.UserListView.as_view(), name='user-list'),
]
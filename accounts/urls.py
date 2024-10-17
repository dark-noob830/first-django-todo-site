from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register_accounts, name='user_register'),
    path('login/', views.login_accounts, name='user_login'),
    path('logout/', views.logout_accounts, name='user_logout'),
]

from django.urls import path
from . import views

urlpatterns = [
path('create-account/', views.create_account, name='create_account'),
path('login/', views.login_user, name='login_user'),
path('dashboard/', views.dashboard, name='dashboard'),
path('logout/', views.logout_user, name='logout_user'),
path('create-profile/', views.create_profile, name='create_profile'),
]
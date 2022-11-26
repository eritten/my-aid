from django.urls import path
from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
path('', views.blog_home, name='blog_home'),
path('detail/<int:pk>/<slug:slug>/<int:year>/<int:month>/<int:day>/', views.detail, name='detail'),
path('terms/', views.terms, name='terms'),
path('privacy/', views.privacy, name='privacy'),
path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
path('search/', views.search, name='search'),
path('feeds/', LatestPostsFeed(), name='feed')
]
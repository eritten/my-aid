from django.contrib import admin
from django.urls import path, include
from homepage import views

urlpatterns = [
path('comment/', include('comment.urls')),
path('', views.home, name='home'),
path('blog/', include('blog.urls')),
path('app/', include('community.urls')),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('', include('home.urls')),
path('app/', include('community.urls')),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path, include
from homepage import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
#path('det/', index, name='index'),
path('comment/', include('comment.urls')),
path('', views.home, name='home'),
path('blog/', include('blog.urls')),
path('app/', include('community.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
  urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

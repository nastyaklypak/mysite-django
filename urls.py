from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    # Припускаємо, що app_blog вже підключений
    path(r'', include('app_blog.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

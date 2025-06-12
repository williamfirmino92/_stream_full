from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sistema.urls')),
    path('usuario/', include('usuarios.urls')),
    path('filme/', include('filmes.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 127.0.0.1:8000/ => A página principal
# 127.0.0.1:8000/admin => A página da tela do django admin





from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inventario/", include("inventario.urls")),
    path('reportes/', include('reportes.urls')),
    
]
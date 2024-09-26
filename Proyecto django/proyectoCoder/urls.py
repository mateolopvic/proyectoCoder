from django.contrib import admin
from django.urls import path
from .views import crear_casa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('guardar-casa/', crear_casa, name='guardar-casa'),
]

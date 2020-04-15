from django.contrib import admin
from django.urls import path
from GestionPedidos import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('busqueda_productos/', views.busqueda_procutos),
    path('buscar/', views.buscar),
]

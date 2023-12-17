from django.contrib import admin
from django.urls import path, include


from .views import Autoridades, AutoridadesDetail , Novedades,NovedadesDetail

urlpatterns = [
    path("autoridades/",Autoridades.as_view(),name="autoridades"),
    path("autoridades/<int:pk>/",AutoridadesDetail.as_view(),name="autoridades_detail"),
    path("novedades/",Novedades.as_view(),name="novedades"),
    path("novedades/<int:pk>/",NovedadesDetail.as_view(),name="novedades_detail"),
]

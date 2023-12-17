from django.contrib import admin
from django.urls import path, include
from .views import JoinCursoView


from .views import curso,normativa,biblioteca_tecnica

urlpatterns = [
    path("curso/",curso.list_view().as_view(),name="curso"),
    path("curso/persona/",curso.per_user_view().as_view(),name="curso_persona"),
    path("curso/<int:pk>/",curso.detail_build().as_view(),name="curso_detail"),


    path('curso/<int:curso_id>/join/', JoinCursoView.as_view(), name='join-curso'),
    path('curso/<int:curso_id>/leave/', JoinCursoView.as_view(), name='leave-curso'),


    path("normativa/",normativa.list_view().as_view(),name="normativa"),
    path("normativa/<int:pk>/",normativa.detail_build().as_view(),name="normativa_detail"),
    
    path("biblioteca/",biblioteca_tecnica.list_view().as_view(),name="biblioteca"),
    path("biblioteca/<int:pk>/",biblioteca_tecnica.detail_build().as_view(),name="biblioteca_detail"),
]

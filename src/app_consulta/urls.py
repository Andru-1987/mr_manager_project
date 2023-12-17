# urls.py
from django.urls import path
from .views import ConsultaListView , ConsultaCreateView

urlpatterns = [
    path('all_by_user/', ConsultaListView.as_view(), name='consultas_list'),
    path('crear_consulta/',ConsultaCreateView.as_view(),name='crear_consulta')
]

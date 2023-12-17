from django.urls import path
from .views import CuotaListView

urlpatterns = [
    path('list/', CuotaListView.as_view(), name='cuotas-list'),
]

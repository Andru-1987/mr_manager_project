from django.urls import path
from .views import UserFileDeleteView

urlpatterns = [
    path('delete/<int:pk>/', UserFileDeleteView.as_view(), name='delete-file'),
]

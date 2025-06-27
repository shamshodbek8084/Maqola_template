# maqola/urls.py
from django.urls import path
from .views import create_maqola, list_maqola, update_maqola, delete_maqola, export_maqola_docx

app_name = 'maqola'  # namespace

urlpatterns = [
    path('create/', create_maqola, name='create'),
    path('list/', list_maqola, name='list'),
    path('update/<int:pk>/', update_maqola, name='update'),
    path('delete/<int:pk>/', delete_maqola, name='delete'),
    path('export/', export_maqola_docx, name='export'),
]

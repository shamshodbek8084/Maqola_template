from django.urls import path
from .views import home, list_maqola, export_maqola_docx, create_maqola

urlpatterns = [
    path('', home, name='home'),
    path('maqolalar/', list_maqola, name='maqola_list'),
    path('maqolalar/export/', export_maqola_docx, name='export_maqola_docx'),
    path('maqolalar/create/', create_maqola, name='maqola_create'),
]

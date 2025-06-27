from django.contrib import admin
from .models import Maqola

@admin.register(Maqola)
class MaqolaAdmin(admin.ModelAdmin):
    list_display = ('title', 'format', 'publication_type', 'journal_name', 'published_date')
    search_fields = ('title', 'journal_name', 'authors')
    list_filter = ('format', 'publication_type', 'published_date')

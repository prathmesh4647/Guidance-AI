from django.contrib import admin
from .models import Idea

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'team', 
        'status',
        'plagiarism_score',
        'created_at'
    )

    list_filter = ('status', 'created_at')
    search_fields = ('title', 'team__name')
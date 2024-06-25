from django.contrib import admin

from . import models

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    search_fields = ('title', 'content')
    list_filter = ('created', 'updated')
    date_hierarchy = 'created'
    ordering = ('-created',)

admin.site.register(models.Notes, NotesAdmin)
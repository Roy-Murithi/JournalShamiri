from django.contrib import admin
from .models import Category, JournalEntry

class JournalAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'content', 'category', 'created_at',)
    list_filter = ('user', 'created_at')
    search_fields = ('user', 'title')
    date_hierarchy = 'created_at'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(JournalEntry, JournalAdmin)
admin.site.register(Category, CategoryAdmin)

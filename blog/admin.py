from django.contrib import admin
from .models import Blog


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'text', 'image')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('created_at',)

admin.site.register(Blog, BlogAdmin)
#admin.site.register(Comment)

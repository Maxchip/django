from django.contrib import admin
from .models import BlogPost

# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published_date')
    list_filter = ('published_date',)
    search_fields = ('title', 'content')
    readonly_fields = ('published_date',)
    ordering = ('-published_date',)
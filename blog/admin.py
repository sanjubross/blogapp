from django.contrib import admin
from .models import Blog, Comment

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "image", "created_at"]


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)
from django.contrib import admin
from .models import Post

class PostDB(admin.ModelAdmin):
    list_display = [
        "title", "text", "author", "created_date", "pub_date"
    ]
admin.site.register(Post, PostDB)
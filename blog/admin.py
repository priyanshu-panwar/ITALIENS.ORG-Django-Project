from django.contrib import admin
from .models import Post, Comment, Social

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Social)
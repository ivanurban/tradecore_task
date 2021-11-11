from django.contrib import admin

from .models import Post, CustomUser, PostLikes,  PostDislikes

# Register your models here.

admin.site.register(Post)

admin.site.register(CustomUser)

admin.site.register(PostLikes)

admin.site.register(PostDislikes)










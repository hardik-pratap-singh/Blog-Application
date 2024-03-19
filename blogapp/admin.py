from django.contrib import admin
from .models import Post
# Register your models here.
# this is where we need to register our models so that they show up on the admin page

admin.site.register(Post)

from django.contrib import admin
from . models import Comment
from html.parser import commentclose

# Register your models here.
admin.site.register(Comment)

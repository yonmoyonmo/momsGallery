from django.contrib import admin
from .models import Photo
from .models import Comment
# Register your models here.

admin.site.register(Photo)
admin.site.register(Comment)

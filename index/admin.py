from django.contrib import admin
from .models import Category, VideoModel, User, Comments


# Register your models here.
admin.site.register(Category)
admin.site.register(VideoModel)
admin.site.register(User)
admin.site.register(Comments)
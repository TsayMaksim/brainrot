from datetime import datetime

from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return str(self.category_name)


class VideoModel(models.Model):
    video_title = models.CharField(max_length=64)
    video_content = models.FileField(upload_to='media')
    video_user = models.CharField(max_length=32)
    video_like = models.IntegerField()
    video_dislike = models.IntegerField()
    video_created_at = models.DateField(default=datetime.date.today)
    video_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.video_title)


class User(models.Model):
    user_name = models.CharField(max_length=64)
    user_phone_number = models.IntegerField()
    user_email = models.EmailField()
    user_password = models.CharField(max_length=32)
    user_password2 = models.CharField(max_length=32)

    def __str__(self):
        return str(self.user_name)


class Comments(models.Model):
    comment_text = models.TextField()
    comment_user = models.CharField(max_length=32)
    comment_video = models.ForeignKey(VideoModel, on_delete=models.CASCADE)
    comment_created_at = models.DateField()

    def __str__(self):
        return str(self.comment_text)
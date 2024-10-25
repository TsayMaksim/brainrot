# Generated by Django 5.1.2 on 2024-10-23 20:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=64)),
                ('user_phone_number', models.IntegerField()),
                ('user_email', models.EmailField(max_length=254)),
                ('user_password', models.CharField(max_length=32)),
                ('user_password2', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=64)),
                ('video_content', models.FileField(upload_to='')),
                ('video_user', models.CharField(max_length=32)),
                ('video_like', models.IntegerField()),
                ('video_dislike', models.IntegerField()),
                ('video_category', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('comment_user', models.CharField(max_length=32)),
                ('comment_created_at', models.DateField()),
                ('comment_video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.videomodel')),
            ],
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-23 23:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_alter_videomodel_video_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='videomodel',
            name='video_created_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
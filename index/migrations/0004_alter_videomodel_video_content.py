# Generated by Django 5.1.2 on 2024-10-23 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_alter_videomodel_video_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videomodel',
            name='video_content',
            field=models.FileField(upload_to='media'),
        ),
    ]

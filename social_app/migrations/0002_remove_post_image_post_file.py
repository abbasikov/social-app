# Generated by Django 4.2.5 on 2023-09-30 15:19

from django.db import migrations, models
import social_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('social_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=social_app.models.get_post_image_filepath),
        ),
    ]

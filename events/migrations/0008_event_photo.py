# Generated by Django 2.2.5 on 2019-11-20 18:50

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_remove_event_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(null=True, upload_to='photos', verbose_name='Главное фото'),
        ),
    ]

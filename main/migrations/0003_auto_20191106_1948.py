# Generated by Django 2.2.5 on 2019-11-06 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191106_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

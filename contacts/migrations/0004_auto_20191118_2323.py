# Generated by Django 2.2.5 on 2019-11-18 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20191118_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_type',
            field=models.CharField(choices=[('P', 'Телефон'), ('E', 'Email')], max_length=50),
        ),
    ]

# Generated by Django 2.2.5 on 2019-11-20 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20191119_0158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='office',
            options={'verbose_name': 'Офис', 'verbose_name_plural': 'Офисы'},
        ),
        migrations.AlterModelOptions(
            name='scheduleitem',
            options={'verbose_name': 'Строка рассписания', 'verbose_name_plural': 'Строки рассписания'},
        ),
    ]

# Generated by Django 2.2.5 on 2019-11-20 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20191119_0158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Событие', 'verbose_name_plural': 'События'},
        ),
        migrations.AlterModelOptions(
            name='eventsection',
            options={'verbose_name': 'Параграф события', 'verbose_name_plural': 'Парагравы события'},
        ),
    ]

# Generated by Django 2.2.5 on 2019-11-21 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20191120_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Значение')),
                ('owner', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец')),
                ('contact_type', models.CharField(choices=[('P', 'Телефон'), ('E', 'Email')], max_length=50, verbose_name='Тип')),
                ('office', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.Office')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50, verbose_name='Заголовок')),
                ('office', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.Office')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.CreateModel(
            name='UnitContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Значение')),
                ('owner', models.CharField(blank=True, default='', max_length=50, verbose_name='Владелец')),
                ('contact_type', models.CharField(choices=[('P', 'Телефон'), ('E', 'Email')], max_length=50, verbose_name='Тип')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contacts.Unit')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]

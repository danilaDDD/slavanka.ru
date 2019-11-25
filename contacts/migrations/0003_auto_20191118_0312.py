# Generated by Django 2.2.5 on 2019-11-18 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20191118_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50)),
                ('owner', models.CharField(blank=True, default='', max_length=50)),
                ('contact_type', models.CharField(max_length=50)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Office')),
            ],
        ),
        migrations.RemoveField(
            model_name='phone',
            name='office',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
        migrations.DeleteModel(
            name='Phone',
        ),
    ]

# Generated by Django 3.2.13 on 2022-07-26 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='sm',
        ),
    ]

# Generated by Django 3.2.13 on 2022-07-31 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='sm',
            field=models.TextField(max_length=800, verbose_name='özet'),
        ),
    ]

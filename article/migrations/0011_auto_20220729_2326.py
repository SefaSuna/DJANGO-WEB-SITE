# Generated by Django 3.2.13 on 2022-07-29 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20220729_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ad',
            field=models.CharField(max_length=50, verbose_name='ad'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='yorum',
            field=models.CharField(max_length=500, verbose_name='yorum'),
        ),
    ]

# Generated by Django 3.2.13 on 2022-08-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_alter_data_sm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.CharField(max_length=80, verbose_name='başlık'),
        ),
    ]
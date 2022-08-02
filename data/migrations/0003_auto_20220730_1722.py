# Generated by Django 3.2.13 on 2022-07-30 14:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20220730_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='data',
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='data.data', verbose_name='article'),
            preserve_default=False,
        ),
    ]

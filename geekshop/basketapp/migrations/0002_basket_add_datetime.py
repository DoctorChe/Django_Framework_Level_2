# Generated by Django 2.1.4 on 2019-01-10 08:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='add_datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='время добавления'),
            preserve_default=False,
        ),
    ]

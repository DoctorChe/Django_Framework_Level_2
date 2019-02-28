# Generated by Django 2.1.4 on 2019-02-27 12:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_shopuser_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128, verbose_name='ключ подтверждения'),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 1, 12, 36, 2, 31448, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-02 22:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20190303_0142'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuserprofile',
            name='site',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 4, 22, 49, 49, 296965, tzinfo=utc), verbose_name='activation key expires'),
        ),
    ]
# Generated by Django 3.0.3 on 2020-02-23 10:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20200223_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2020, 2, 23, 10, 57, 37, 359434, tzinfo=utc)),
        ),
    ]

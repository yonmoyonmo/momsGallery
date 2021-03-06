# Generated by Django 3.0.3 on 2020-03-22 07:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django_resized.forms
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_auto_20200223_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=25, size=[1920, 1080], upload_to=gallery.models.user_path),
        ),
        migrations.AlterField(
            model_name='photo',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2020, 3, 22, 7, 24, 17, 743050, tzinfo=utc)),
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-23 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='thumname_image',
        ),
    ]
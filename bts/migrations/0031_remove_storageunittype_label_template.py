# Generated by Django 4.2.1 on 2023-05-26 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bts', '0030_delete_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storageunittype',
            name='label_template',
        ),
    ]

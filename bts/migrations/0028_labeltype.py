# Generated by Django 4.2.1 on 2023-05-21 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bts', '0027_location_assortmentbox_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabelType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('lines_per_row', models.IntegerField()),
                ('rows_per_label', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]

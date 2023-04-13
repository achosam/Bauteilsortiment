# Generated by Django 4.1.7 on 2023-04-13 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bts', '0016_alter_inventory_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='purchase',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='purchase',
            constraint=models.UniqueConstraint(fields=('merchant', 'order_number'), name='UQ_Purchase_merchant_oder_number'),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-20 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_subcribers_date_alter_tiplogopost_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcribers',
            name='date',
            field=models.DateTimeField(db_default=models.Value(datetime.datetime(2024, 1, 20, 14, 22, 13, 346464))),
        ),
        migrations.AlterField(
            model_name='tiplogopost',
            name='updated_at',
            field=models.DateTimeField(db_default=models.Value(datetime.datetime(2024, 1, 20, 14, 22, 13, 362092))),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-17 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_tiplogopost_alter_subcribers_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcribers',
            name='date',
            field=models.DateTimeField(db_default=models.Value(datetime.datetime(2024, 1, 17, 20, 46, 13, 308292))),
        ),
        migrations.AlterField(
            model_name='tiplogopost',
            name='updated_at',
            field=models.DateTimeField(db_default=models.Value(datetime.datetime(2024, 1, 17, 20, 46, 13, 308292))),
        ),
    ]

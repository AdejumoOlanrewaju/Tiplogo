# Generated by Django 5.0.1 on 2024-03-31 04:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_fishpost_jambpost_alter_subcribers_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishpost',
            name='updated_at',
            field=models.DateTimeField(db_default=models.Value(datetime.datetime(2024, 3, 30, 21, 40, 44, 926804))),
        ),
        migrations.AlterField(
            model_name='jambpost',
            name='updated_at',
            field=models.DateTimeField(db_default=models.Value(datetime.datetime(2024, 3, 30, 21, 40, 44, 926804))),
        ),
        migrations.AlterField(
            model_name='subcribers',
            name='date',
            field=models.DateTimeField(db_default=models.Value(datetime.datetime(2024, 3, 30, 21, 40, 44, 926804))),
        ),
        migrations.AlterField(
            model_name='tiplogopost',
            name='updated_at',
            field=models.DateTimeField(db_default=models.Value(datetime.datetime(2024, 3, 30, 21, 40, 44, 926804))),
        ),
    ]

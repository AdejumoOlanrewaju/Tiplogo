# Generated by Django 5.0.1 on 2024-01-17 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_emailtemplate_subcriber_alter_subcribers_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailtemplate',
            name='subcriber',
        ),
        migrations.AlterField(
            model_name='subcribers',
            name='date',
            field=models.DateTimeField(db_default=models.Value(datetime.datetime(2024, 1, 17, 14, 13, 38, 254136))),
        ),
    ]

# Generated by Django 4.2.4 on 2023-12-02 23:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0011_event_deny_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 2, 23, 9, 11, 855084, tzinfo=datetime.timezone.utc)),
        ),
    ]

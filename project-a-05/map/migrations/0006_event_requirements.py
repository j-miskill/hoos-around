# Generated by Django 4.2.4 on 2023-11-06 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_merge_0003_alter_event_user_0004_alter_event_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='requirements',
            field=models.CharField(default='', max_length=500),
        ),
    ]

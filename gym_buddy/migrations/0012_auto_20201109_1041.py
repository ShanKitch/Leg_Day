# Generated by Django 2.2 on 2020-11-09 17:41

from django.db import migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_buddy', '0011_auto_20201101_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location_state',
            field=localflavor.us.models.USStateField(max_length=2),
        ),
    ]

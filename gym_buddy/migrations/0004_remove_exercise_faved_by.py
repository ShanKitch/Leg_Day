# Generated by Django 2.2 on 2020-10-09 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_buddy', '0003_exercise_faved_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='faved_by',
        ),
    ]

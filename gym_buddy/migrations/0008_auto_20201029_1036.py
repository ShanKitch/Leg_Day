# Generated by Django 2.2 on 2020-10-29 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gym_buddy', '0007_message_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='receiver',
            new_name='recipient',
        ),
    ]

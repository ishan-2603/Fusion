# Generated by Django 3.1.5 on 2024-04-06 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr2', '0005_leaveform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaveform',
            old_name='Dealing_Assistant',
            new_name='dealing_assistant',
        ),
        migrations.RenameField(
            model_name='leaveform',
            old_name='Deputy_Registrar',
            new_name='deputy_registrar',
        ),
    ]

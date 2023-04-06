# Generated by Django 3.1.5 on 2023-03-31 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_information', '0001_initial'),
        ('central_mess', '0002_auto_20230328_1942'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='payments',
            unique_together={('student_id',)},
        ),
        migrations.RemoveField(
            model_name='payments',
            name='sem',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='year',
        ),
    ]
# Generated by Django 3.1.5 on 2024-04-06 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr2', '0006_auto_20240406_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appraisalform',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_id', models.IntegerField(max_length=22, null=True)),
                ('name', models.CharField(max_length=22, null=True)),
                ('designation', models.CharField(max_length=50, null=True)),
                ('discipline', models.CharField(max_length=22, null=True)),
                ('field_knowledge', models.CharField(max_length=40, null=True)),
                ('current_res_int', models.CharField(max_length=40, null=True)),
                ('courses_taught', models.CharField(max_length=100, null=True)),
                ('new_courses_introduced', models.CharField(max_length=100, null=True)),
                ('new_courses_developed', models.CharField(max_length=100, null=True)),
                ('instructional_tasks', models.CharField(max_length=100, null=True)),
                ('thesis_reasearch', models.CharField(max_length=100, null=True)),
                ('sponsored_research', models.CharField(max_length=100, null=True)),
                ('research_element', models.CharField(max_length=40, null=True)),
                ('Publication', models.CharField(max_length=40, null=True)),
                ('referred_conf', models.CharField(max_length=40, null=True)),
                ('conf_organised', models.CharField(max_length=40, null=True)),
                ('memberships', models.CharField(max_length=40, null=True)),
                ('honours', models.CharField(max_length=40, null=True)),
                ('edt_of_rep_pub', models.CharField(max_length=40, null=True)),
                ('expert_lec_del', models.CharField(max_length=40, null=True)),
                ('mem_of_bos', models.CharField(max_length=40, null=True)),
                ('extention_tasks', models.CharField(max_length=40, null=True)),
                ('add_assign', models.CharField(max_length=40, null=True)),
                ('service_inst_community', models.CharField(max_length=40, null=True)),
                ('other_contri', models.CharField(max_length=40, null=True)),
                ('your_comments', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(max_length=6, null=True)),
                ('sign_faculty', models.CharField(max_length=40, null=True)),
                ('remarks', models.CharField(max_length=40, null=True)),
                ('sign_HOD', models.CharField(max_length=40, null=True)),
                ('sign_director', models.CharField(max_length=40, null=True)),
            ],
        ),
    ]

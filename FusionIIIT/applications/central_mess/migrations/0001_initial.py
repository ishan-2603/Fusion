# Generated by Django 3.1.5 on 2024-04-15 23:58

import applications.central_mess.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic_information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mess_option', models.CharField(choices=[('mess1', 'Mess1'), ('mess2', 'Mess2')], default='mess2', max_length=20)),
                ('meal_time', models.CharField(choices=[('MB', 'Monday Breakfast'), ('ML', 'Monday Lunch'), ('MD', 'Monday Dinner'), ('TB', 'Tuesday Breakfast'), ('TL', 'Tuesday Lunch'), ('TD', 'Tuesday Dinner'), ('WB', 'Wednesday Breakfast'), ('WL', 'Wednesday Lunch'), ('WD', 'Wednesday Dinner'), ('THB', 'Thursday Breakfast'), ('THL', 'Thursday Lunch'), ('THD', 'Thursday Dinner'), ('FB', 'Friday Breakfast'), ('FL', 'Friday Lunch'), ('FD', 'Friday Dinner'), ('SB', 'Saturday Breakfast'), ('SL', 'Saturday Lunch'), ('SD', 'Saturday Dinner'), ('SUB', 'Sunday Breakfast'), ('SUL', 'Sunday Lunch'), ('SUD', 'Sunday Dinner')], max_length=20)),
                ('dish', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mess_meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meet_date', models.DateField()),
                ('agenda', models.TextField()),
                ('venue', models.TextField()),
                ('meeting_time', models.CharField(choices=[('10', '10 a.m.'), ('11', '11 a.m.'), ('12', '12 p.m.'), ('13', '1 p.m.'), ('14', '2 p.m.'), ('15', '3 p.m.'), ('16', '4 p.m.'), ('17', '5 p.m.'), ('18', '6 p.m.'), ('19', '7 p.m.'), ('20', '8 p.m.'), ('21', '9 p.m.')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mess_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sem', models.IntegerField(default='1')),
                ('start_reg', models.DateField(default=datetime.date.today)),
                ('end_reg', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='MessBillBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_amount', models.PositiveIntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vacation_food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('purpose', models.TextField()),
                ('status', models.CharField(choices=[('0', 'rejected'), ('1', 'pending'), ('2', 'accepted')], default='1', max_length=20)),
                ('app_date', models.DateField(default=datetime.date.today)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Special_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('request', models.TextField()),
                ('status', models.CharField(choices=[('0', 'rejected'), ('1', 'pending'), ('2', 'accepted')], default='1', max_length=20)),
                ('item1', models.CharField(choices=[('dal_chawal', 'Dal Chawal'), ('khicdi', 'Khicdi'), ('tomato_soup', 'Tomato Soup')], default='dal_chawal', max_length=50)),
                ('item2', models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')], default='breakfast', max_length=50)),
                ('app_date', models.DateField(default=datetime.date.today)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Semdates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'unique_together': {('start_date', 'end_date')},
            },
        ),
        migrations.CreateModel(
            name='Registration_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Txn_no', models.CharField(max_length=20)),
                ('img', models.ImageField(default=None, upload_to='images/')),
                ('amount', models.IntegerField(default=0)),
                ('status', models.CharField(default='pending', max_length=10)),
                ('registration_remark', models.CharField(default='NA', max_length=50)),
                ('start_date', models.DateField(default=None, null=True)),
                ('payment_date', models.DateField(default=None, null=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Reg_records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=None, null=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Reg_main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=10)),
                ('current_mess_status', models.CharField(default='Deregistered', max_length=20)),
                ('balance', models.IntegerField(default=0)),
                ('mess_option', models.CharField(default='mess2', max_length=20)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Rebate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('purpose', models.TextField()),
                ('status', models.CharField(choices=[('0', 'rejected'), ('1', 'pending'), ('2', 'accepted')], default='1', max_length=20)),
                ('app_date', models.DateField(default=datetime.date.today)),
                ('leave_type', models.CharField(choices=[('casual', 'Casual'), ('vacation', 'Vacation')], default='casual', max_length=20)),
                ('rebate_remark', models.CharField(default='NA', max_length=50)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Mess_minutes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mess_minutes', models.FileField(upload_to='central_mess/')),
                ('meeting_date', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='central_mess.mess_meeting')),
            ],
        ),
        migrations.CreateModel(
            name='Menu_change_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('request', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('0', 'rejected'), ('1', 'pending'), ('2', 'accepted')], default='1', max_length=20)),
                ('app_date', models.DateField(default=datetime.date.today)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='central_mess.menu')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mess', models.CharField(choices=[('mess1', 'Mess1'), ('mess2', 'Mess2')], default='mess1', max_length=10)),
                ('mess_rating', models.PositiveSmallIntegerField(default='5')),
                ('fdate', models.DateField(default=datetime.date.today)),
                ('description', models.TextField()),
                ('feedback_type', models.CharField(choices=[('maintenance', 'Maintenance'), ('food', 'Food'), ('cleanliness', 'Cleanliness & Hygiene'), ('others', 'Others')], max_length=20)),
                ('feedback_remark', models.CharField(default='NA', max_length=50)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Deregistration_Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='pending', max_length=10)),
                ('deregistration_remark', models.CharField(default='NA', max_length=50)),
                ('end_date', models.DateField(default=None, null=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.IntegerField(default=0)),
                ('payment_month', models.CharField(default=applications.central_mess.models.current_month, max_length=20)),
                ('payment_year', models.IntegerField(default=applications.central_mess.models.current_year)),
                ('payment_date', models.DateField(default=datetime.date(2024, 4, 15))),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
            options={
                'unique_together': {('student_id', 'payment_date')},
            },
        ),
        migrations.CreateModel(
            name='Monthly_bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(default=applications.central_mess.models.current_month, max_length=20)),
                ('year', models.IntegerField(default=applications.central_mess.models.current_year)),
                ('amount', models.IntegerField(default=0)),
                ('rebate_count', models.IntegerField(default=0)),
                ('rebate_amount', models.IntegerField(default=0)),
                ('total_bill', models.IntegerField(default=0)),
                ('paid', models.BooleanField(default=False)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
            options={
                'unique_together': {('student_id', 'month', 'year')},
            },
        ),
        migrations.CreateModel(
            name='Messinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mess_option', models.CharField(choices=[('mess1', 'Mess1'), ('mess2', 'Mess2')], default='mess2', max_length=20)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academic_information.student')),
            ],
            options={
                'unique_together': {('student_id', 'mess_option')},
            },
        ),
    ]
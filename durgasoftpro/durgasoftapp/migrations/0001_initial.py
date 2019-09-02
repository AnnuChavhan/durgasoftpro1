# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-29 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnquiryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('courses', multiselectfield.db.fields.MultiSelectField(max_length=200, verbose_name=(('py', 'python'), ('dj', 'django'), ('py', 'Rest Api'), ('fl', 'Flask'), ('UI', 'Ui')))),
                ('shifts', multiselectfield.db.fields.MultiSelectField(max_length=200, verbose_name=(('Moring', 'Moring Shift'), ('Afternoon', 'Afternoon shift'), ('Evening', 'Evening Shift'), ('Night', 'Night Shift')))),
                ('start_date', models.DateTimeField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField(max_length=100)),
                ('feedback', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServicesData',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100, unique=True)),
                ('course_duration', models.CharField(max_length=100)),
                ('course_state_date', models.DateField(max_length=100)),
                ('course_start_time', models.TimeField(max_length=100)),
                ('course_trainer_name', models.CharField(max_length=100)),
                ('course_trainer_exp', models.CharField(max_length=100)),
            ],
        ),
    ]
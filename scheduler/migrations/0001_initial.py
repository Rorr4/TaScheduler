# Generated by Django 5.0.4 on 2024-05-15 00:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=30)),
                ('time', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=30, null=True)),
                ('lastName', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('userType', models.CharField(blank=True, max_length=20, null=True)),
                ('skills', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SectionTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('time', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LabTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectionNumber', models.CharField(max_length=30)),
                ('time', models.CharField(blank=True, max_length=30, null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.sectiontable')),
            ],
        ),
        migrations.CreateModel(
            name='UserSectionJoinTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.sectiontable')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.usertable')),
            ],
        ),
        migrations.CreateModel(
            name='UserLabJoinTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.labtable')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.usertable')),
            ],
        ),
        migrations.CreateModel(
            name='UserCourseJoinTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.coursetable')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduler.usertable')),
            ],
        ),
    ]

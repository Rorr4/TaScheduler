# Generated by Django 5.0.4 on 2024-05-15 00:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectiontable',
            name='courseId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='scheduler.coursetable'),
            preserve_default=False,
        ),
    ]

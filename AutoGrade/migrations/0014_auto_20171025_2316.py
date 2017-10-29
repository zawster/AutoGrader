# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-25 18:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AutoGrade', '0013_auto_20171001_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=64)),
                ('moss_name', models.CharField(default=None, max_length=64)),
                ('compile_cmd', models.CharField(default=None, max_length=255)),
                ('execution_cmd', models.CharField(default=None, max_length=255)),
                ('executable_name', models.CharField(default=None, max_length=255)),
                ('is_interpreted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AutoGrade.Language'),
        ),
    ]

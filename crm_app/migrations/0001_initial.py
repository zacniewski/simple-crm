# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-04 17:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=50)),
                ('sector', models.CharField(choices=[('IT', 'IT'), ('Finance', 'Finance'), ('Education', 'Education')], default='IT', max_length=10)),
                ('number_of_employees', models.CharField(choices=[('1-20', '1-20'), ('21-50', '21-50'), ('51-100', '51-100'), ('>100', '>100')], default='21-50', max_length=10)),
                ('added_by', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CrmUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

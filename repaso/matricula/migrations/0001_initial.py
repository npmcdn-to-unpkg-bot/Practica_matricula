# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-19 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('cedula', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=30)),
                ('direccion', models.TextField(default='direccion', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('horas', models.CharField(max_length=20)),
                ('creditos', models.CharField(max_length=20)),
                ('num_cupos', models.CharField(max_length=20)),
            ],
        ),
    ]

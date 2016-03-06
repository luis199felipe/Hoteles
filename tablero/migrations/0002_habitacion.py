# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablero', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_habitacion', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('hotel', models.ForeignKey(to='tablero.Hotel')),
            ],
        ),
    ]

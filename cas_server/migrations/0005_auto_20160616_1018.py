# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 10:18
from __future__ import unicode_literals

from django.db import migrations, models
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cas_server', '0004_auto_20151218_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='FederatedUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=124)),
                ('provider', models.CharField(max_length=124)),
                ('attributs', picklefield.fields.PickledObjectField(editable=False)),
                ('ticket', models.CharField(max_length=255)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='federateduser',
            unique_together=set([('username', 'provider')]),
        ),
    ]
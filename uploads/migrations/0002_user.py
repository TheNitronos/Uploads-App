# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nom', models.CharField(max_length=20, default='User')),
                ('theme', models.CharField(max_length=1, default='a')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

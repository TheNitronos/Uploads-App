# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('image', models.ImageField(upload_to='uploadedImages')),
                ('tag', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500, null=True)),
                ('saturation', models.DecimalField(max_digits=2, decimal_places=1, default=0)),
                ('contraste', models.DecimalField(max_digits=2, decimal_places=1, default=0)),
                ('luminosite', models.DecimalField(max_digits=2, decimal_places=1, default=0)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

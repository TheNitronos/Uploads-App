# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('image', models.ImageField(upload_to='uploadedImages')),
                ('tag', models.CharField(max_length=30)),
                ('description', models.CharField(null=True, max_length=500)),
                ('saturation', models.DecimalField(decimal_places=1, max_digits=2, default=0)),
                ('contraste', models.DecimalField(decimal_places=1, max_digits=2, default=0)),
                ('luminosite', models.DecimalField(decimal_places=1, max_digits=2, default=0)),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('theme', models.CharField(max_length=1, default='a')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('theme', models.CharField(max_length=1, default='a')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='picture',
            name='uploader',
            field=models.ForeignKey(to='uploads.Student'),
            preserve_default=True,
        ),
    ]

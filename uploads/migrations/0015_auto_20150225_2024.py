# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uploads', '0014_auto_20150225_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('avatar', models.ImageField(blank=True, upload_to='avatars/', null=True)),
                ('theme', models.CharField(max_length=1)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('avatar', models.ImageField(blank=True, upload_to='avatars/', null=True)),
                ('theme', models.CharField(max_length=1)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Theme',
        ),
        migrations.AddField(
            model_name='picture',
            name='proprietaire',
            field=models.OneToOneField(to='uploads.Student', null=True),
            preserve_default=True,
        ),
    ]

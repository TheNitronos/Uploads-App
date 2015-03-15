# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('uploads', '0017_auto_20150312_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nom', models.TextField(blank=True)),
                ('prenom', models.TextField(blank=True)),
                ('pseudo', models.TextField(max_length=30)),
                ('theme', models.TextField(max_length=1, default='a')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='profil',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='picture',
            name='description',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]

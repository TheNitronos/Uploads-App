# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_auto_20150320_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='corrige',
            field=models.ImageField(upload_to='corriges', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tag',
            name='donnee',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tag',
            name='exercice',
            field=models.ImageField(upload_to='exercices', null=True),
            preserve_default=True,
        ),
    ]

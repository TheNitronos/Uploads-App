# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0007_auto_20150114_2355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='exercises',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='sender',
        ),
        migrations.AddField(
            model_name='picture',
            name='contraste',
            field=models.DecimalField(default=0, max_digits=2, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='luminosite',
            field=models.DecimalField(default=0, max_digits=2, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='picture',
            name='saturation',
            field=models.DecimalField(default=0, max_digits=2, decimal_places=2),
            preserve_default=True,
        ),
    ]

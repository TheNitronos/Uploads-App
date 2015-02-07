# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0008_auto_20150207_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='contraste',
            field=models.DecimalField(default=0, decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='picture',
            name='luminosite',
            field=models.DecimalField(default=0, decimal_places=1, max_digits=2),
        ),
        migrations.AlterField(
            model_name='picture',
            name='saturation',
            field=models.DecimalField(default=0, decimal_places=1, max_digits=2),
        ),
    ]

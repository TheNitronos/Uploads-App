# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cameraUpload', '0006_auto_20141214_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='classe',
            field=models.CharField(null=True, max_length=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pictures',
            name='tag',
            field=models.CharField(null=True, max_length=200),
            preserve_default=True,
        ),
    ]

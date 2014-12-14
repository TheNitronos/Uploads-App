# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cameraUpload', '0003_auto_20141211_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='image',
            field=models.ImageField(upload_to='', height_field='150', width_field='200'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cameraUpload', '0004_auto_20141211_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]

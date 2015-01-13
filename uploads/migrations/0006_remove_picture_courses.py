# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0005_auto_20150107_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='courses',
        ),
    ]

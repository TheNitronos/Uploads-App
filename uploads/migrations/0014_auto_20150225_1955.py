# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0013_theme'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]

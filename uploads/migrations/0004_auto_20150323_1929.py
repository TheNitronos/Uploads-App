# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0003_auto_20150322_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='corrige',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='donnee',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='exercice',
        ),
    ]

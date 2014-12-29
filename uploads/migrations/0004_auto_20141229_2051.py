# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0003_auto_20141225_2050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='exercice_topic',
            new_name='exercise_topic',
        ),
    ]

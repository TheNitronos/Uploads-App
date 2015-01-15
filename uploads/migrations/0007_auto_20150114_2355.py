# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0006_remove_picture_courses'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picture',
            old_name='owner',
            new_name='sender',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='receiver',
        ),
    ]

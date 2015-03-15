# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uploads.models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0018_auto_20150315_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='proprietaire',
            field=models.ForeignKey(to='uploads.Profil', default=uploads.models.Profil),
            preserve_default=True,
        ),
    ]

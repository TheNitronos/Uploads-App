# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0020_auto_20150315_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='proprietaire',
            field=models.ForeignKey(to='uploads.Profil'),
        ),
    ]

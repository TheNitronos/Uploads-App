# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0019_picture_proprietaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='proprietaire',
            field=models.ForeignKey(to='uploads.Profil', default='anonyme'),
        ),
    ]

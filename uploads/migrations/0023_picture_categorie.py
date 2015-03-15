# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0022_remove_picture_proprietaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='categorie',
            field=models.ForeignKey(to='uploads.Profil', default='anonyme'),
            preserve_default=False,
        ),
    ]

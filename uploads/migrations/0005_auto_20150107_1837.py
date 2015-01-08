# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0004_auto_20141229_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='owner',
            field=models.ForeignKey(to='uploads.Student', null=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='receiver',
            field=models.ForeignKey(to='uploads.Teacher', null=True),
        ),
    ]

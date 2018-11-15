# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='dni',
            field=models.CharField(max_length=40, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='fecha_Nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]

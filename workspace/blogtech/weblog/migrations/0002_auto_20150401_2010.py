# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='tagname',
            field=models.CharField(blank=True, max_length=20, null=True),
            preserve_default=True,
        ),
    ]

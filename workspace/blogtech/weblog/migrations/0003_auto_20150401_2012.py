# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0002_auto_20150401_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_modified',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tags',
            name='tagname',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]

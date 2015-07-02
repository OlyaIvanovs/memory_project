# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memory_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='value',
            field=models.CharField(default=2, max_length=10, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')]),
            preserve_default=True,
        ),
    ]

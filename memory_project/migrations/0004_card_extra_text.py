# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memory_project', '0003_auto_20150623_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='extra_text',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]

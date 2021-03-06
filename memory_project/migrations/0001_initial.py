# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_side_text', models.CharField(max_length=200)),
                ('second_side_text', models.CharField(max_length=200)),
                ('show_date', models.DateTimeField(verbose_name=b'show date')),
                ('value', models.CharField(default=2, max_length=2, choices=[(0, b'0'), (1, b'1'), (2, b'2'), (3, b'3'), (4, b'4'), (5, b'5')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

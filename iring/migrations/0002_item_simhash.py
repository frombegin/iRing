# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('iring', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='simhash',
            field=models.CharField(default=datetime.datetime(2016, 1, 22, 4, 55, 30, 786000, tzinfo=utc), max_length=16),
            preserve_default=False,
        ),
    ]

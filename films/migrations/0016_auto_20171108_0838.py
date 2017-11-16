# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0015_auto_20171107_0934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genres',
            old_name='genre',
            new_name='genres',
        ),
    ]

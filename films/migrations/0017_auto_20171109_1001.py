# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0016_auto_20171108_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genres',
            name='genres',
            field=models.TextField(verbose_name='Жанр'),
        ),
    ]

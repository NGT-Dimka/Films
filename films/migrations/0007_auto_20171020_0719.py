# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_auto_20171019_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='id_film',
        ),
        migrations.AddField(
            model_name='film',
            name='id',
            field=models.AutoField(default=0, serialize=False, verbose_name='ID', auto_created=True, primary_key=True),
            preserve_default=False,
        ),
    ]

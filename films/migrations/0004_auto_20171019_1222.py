# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_remove_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='id_film',
            field=models.IntegerField(unique=True, primary_key=True, serialize=False),
        ),
    ]

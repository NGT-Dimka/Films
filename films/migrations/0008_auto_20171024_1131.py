# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_auto_20171020_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='poster',
            field=models.ImageField(blank=True, verbose_name='Постер фильма', upload_to='films/media/films/Posters/'),
        ),
    ]

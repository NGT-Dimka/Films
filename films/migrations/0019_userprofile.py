# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('films', '0018_auto_20171110_0824'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('location', models.CharField(verbose_name='Населенный пункт:', max_length=100, blank=True)),
                ('birth_date', models.DateField(verbose_name='Дата рождения:', blank=True)),
                ('avatar', models.ImageField(verbose_name='Аватар:', upload_to='')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

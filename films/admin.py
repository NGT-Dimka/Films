# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from films.models import Film, Producer, Comment, Genres

admin.site.register(Film)
admin.site.register(Producer)
admin.site.register(Comment)
admin.site.register(Genres)

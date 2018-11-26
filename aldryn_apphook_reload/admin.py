# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from .models import UrlconfRevision


class UrlconfAdmin(admin.ModelAdmin):
    list_display = (
        'revision',
    )


admin.site.register(UrlconfRevision, UrlconfAdmin)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from .models import UrlconfRevision
from django.contrib import admin


class UrlconfAdmin(admin.ModelAdmin):
    list_display = (
        'revision',
    )


admin.site.register(UrlconfRevision, UrlconfAdmin)

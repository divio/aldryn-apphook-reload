# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models

from . import signals  # needed for signal registration


class UrlconfRevision(models.Model):
    revision = models.CharField(max_length=255)

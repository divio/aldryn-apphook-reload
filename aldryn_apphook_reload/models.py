# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.db import models

from . import signals  # needed for signal registration


class UrlconfRevision(models.Model):
    revision = models.CharField(max_length=255)

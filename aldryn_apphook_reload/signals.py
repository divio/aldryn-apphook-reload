# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import cms.signals
from . import utils


def trigger_server_restart(**kwargs):
    utils.mark_urlconf_as_changed()


cms.signals.urls_need_reloading.connect(
    trigger_server_restart, dispatch_uid='aldryn-apphook-reload-handle-urls-need-reloading')

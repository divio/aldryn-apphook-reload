# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class MyTestApphook(CMSApp):
    name = _("My Apphook")
    urls = ["aldryn_apphook_reload.test_utils.test_app.urls"]

apphook_pool.register(MyTestApphook)

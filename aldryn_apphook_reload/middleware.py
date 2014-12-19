# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from . import utils


class ApphookReloadMiddleware(object):
    """
    redirects any alias domains to the main domain.
    Takes into account if SECURE_SSL_REDIRECT (from django-secure) is set and redirects directly to the
    https version of the main domain if that is true.

    This middleware must be BEFORE djangosecure.middleware.SecurityMiddleware in MIDDLEWARE_CLASSES, so it can
    prevent the redirect from an alias domain to it's https version by djangosecure.middleware.SecurityMiddleware,
    because you might only cover the main domain with the certificate.
    """
    def process_request(self, request):
        utils.ensure_urlconf_is_up_to_date()

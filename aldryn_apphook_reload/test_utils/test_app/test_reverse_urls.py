# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.http import HttpResponse
from django.views.generic import View

from aldryn_apphook_reload.compat import reverse, urlresolvers


class MyTestView(View):
    def get(self, request, *args, **kwargs):
        try:
            url1 = reverse('my_test_app_view')
            url2 = urlresolvers.reverse('my_test_app_view')
            if url1 == url2:
                url = url1
            else:
                raise Exception('urls not the same!!!!')
        except Exception as e:
            url = 'failed: {}'.format(e)
        return HttpResponse("Apphook Test: {}".format(url))


urlpatterns = [
    url(r'^$', MyTestView.as_view(), name='my_test_app_view_test'),
]

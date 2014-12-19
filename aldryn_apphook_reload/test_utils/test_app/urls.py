# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.views.generic import View


class MyTestView(View):
    def get(self, request, *args, **kwargs):
        try:
            url = reverse('my_test_app_view')
        except Exception as e:
            url = 'failed: {}'.format(e)
        # return HttpResponse("My Apphook Page (resolving to {})".format(url))
        return HttpResponse("My Apphook Page")


urlpatterns = patterns('',
    url(r'^$', MyTestView.as_view(), name='my_test_app_view'),
)

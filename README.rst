aldryn-apphook-reload
=====================

.. image:: https://travis-ci.org/aldryn/aldryn-apphook-reload.svg?branch=develop
    :target: https://travis-ci.org/aldryn/aldryn-apphook-reload

.. image:: https://img.shields.io/coveralls/aldryn/aldryn-apphook-reload.svg
  :target: https://coveralls.io/r/aldryn/aldryn-apphook-reload

Reload urls of django CMS Apphooks without a restart


.. warning:: This is a Prototype.


Introduction
------------

Django CMS allows `extending cms pages with Apphooks
<http://django-cms.readthedocs.org/en/support-3.0.x/introduction/apphooks.html>`_.
Apphooks are saved in the Database, which means urls depend on the database contents. For changes
to Apphooks to be reflected in ``reverse()`` and ``{% url ... %}`` calls, a webserver restart
is usually necessary.

aldryn-apphook-reload will automatically reload urls from Django CMS apphooks, without the need
of a webserver restart. It listens to ``cms.signals.urls_need_reloading`` and causes a reload.

The signal is only available in the process where the change to the database was made. In order
for other processes to know when to reload (be it a gunicorn worker or a process on a other server)
a token is saved in the database. This implies a performance hit: 1 database query per request.


Installation
------------

* add ``aldryn_apphook_reload`` to ``INSTALLED_APPS``.

* add ``aldryn_apphook_reload.middleware.ApphookReloadMiddleware`` to ``MIDDLEWARE_CLASSES``
  (place it as close to the top as possible)

* run migrations: ``python manage.py migrate aldryn_apphook_reload``

**Note:** for ``Django<1.7`` you also need to install and configure ``South``
to be able to run migrations.

Advanced
--------

If the process that triggers ``cms.signals.urls_need_reloading`` is a simple ``runserver`` under
load ( ~2 requests per second), the reload sometimes fails on the other processes. This might be
due to an unknown race condition, where the token in the database is refreshed already, but the
new apphooks are not in the database yet. The other processes would try to reload right away
and would reload the old apphooks.
Tests with gunicorn in the default mode and in the gevent mode worked fine though.

Why not save the token in the cache backend for better performance? - Because altering the cache
would happen right away, before the database transaction is committed at the end of the request.
Thus other process would reload their urls prematurely.





try:
    # Django>=2.0
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

try:
    # Django>=2.0
    import django.urls as urlresolvers
except ImportError:
    import django.core.urlresolvers as urlresolvers

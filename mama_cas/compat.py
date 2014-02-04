from django.conf import settings


__all__ = ['user_model', 'SiteProfileNotAvailable']


# Django >= 1.5 uses AUTH_USER_MODEL to specify the currently active
# User model. Previous versions of Django do not have this setting
# and use the built-in User model.
#
# This is not needed when support for Django 1.4 is dropped.
user_model = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


# The SiteProfileNotAvailable exception is raised from get_profile()
# when AUTH_PROFILE_MODULE is unavailable or invalid. With the
# arrival of custom User models in Django 1.5 this exception was
# deprecated, and removed entirely in Django 1.7.
#
# This is not needed when support for Django <= 1.6 is dropped.
try:
    from django.contrib.auth.models import SiteProfileNotAvailable
except ImportError:  # pragma: no cover
    class SiteProfileNotAvailable(Exception):
        pass
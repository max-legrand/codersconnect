from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
# from simple_decorators.apps.models import Entry


def is_org(function):
    def wrap(request, *args, **kwargs):
        # entry = Entry.objects.get(pk=kwargs['entry_id'])
        try:
            if request.user.organization:
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        except Exception:
            return redirect("home")
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def is_user(function):
    def wrap(request, *args, **kwargs):
        # entry = Entry.objects.get(pk=kwargs['entry_id'])
        try:
            if request.user.extendeduser:
                return function(request, *args, **kwargs)
            else:
                raise PermissionDenied
        except Exception:
            return redirect("home")
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
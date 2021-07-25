from django.http import HttpResponse
from django.shortcuts import redirect


# prevents logged in users accessing some views
def unauthenticated_user(view_fn):
    def wrapper_fn(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('get_account', str(request.user.id))
        else:
            return view_fn(request, *args, **kwargs)

    return wrapper_fn


def allowed_users(allowed_roles=[]):
    def decorator(view_fn):
        def wrapper_fn(request, *args, **kwargs):
            if request.user.groups.filter(name__in=allowed_roles).exists():
                return view_fn(request, *args, **kwargs)
            else:
                return HttpResponse('Account does not have authorisation for access', status=401)
        return wrapper_fn
    return decorator

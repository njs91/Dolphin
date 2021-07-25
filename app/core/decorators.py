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


def allowed_users(allowed_roles=[], own_account_only=False):
    def decorator(view_fn):
        def wrapper_fn(request, *args, **kwargs):
            # if the user doesn't own the account and is not an admin
            if own_account_only is True and int(kwargs.get('pk')) is not request.user.id and not request.user.groups.filter(name__in=['admin']).exists():
                return HttpResponse('Account does not have authorisation for access', status=401)
            if request.user.groups.filter(name__in=allowed_roles).exists():
                return view_fn(request, *args, **kwargs)
            else:
                return HttpResponse('Account does not have authorisation for access', status=401)
        return wrapper_fn
    return decorator

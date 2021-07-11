from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_fn):
    def wrapper_fn(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('get_account', str(request.user.id))
        else:
            return view_fn(request, *args, **kwargs)

    return wrapper_fn

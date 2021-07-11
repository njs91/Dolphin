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
            print('roles', allowed_roles)
            group = None
            # check if user is part of a group
            if request.user.groups.exists():  # if list exists
                # set group value to first group in list
                group = request.user.groups.all()[0].name
                # @todo: really [0]?

            if group in allowed_roles:
                return view_fn(request, *args, **kwargs)
            else:
                return HttpResponse('Account does not have authorisation for access')
        return wrapper_fn
    return decorator

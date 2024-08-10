from django.http import HttpResponseForbidden
from functools import wraps

def check_permission(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.profile.position == 'crew':
            return HttpResponseForbidden("Anda tidak memiliki akses ke halaman ini.")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user. is_authenticated:
            return redirect('reports:admin_dashboard')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse ('You are not allowed')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group  == 'student':
            return redirect('reports:student_dashboard')

        if group  == 'counsellor':
            return redirect('reports:counsellor_dashboard')

        if group  == 'trainer':
            return redirect('reports:trainer_dashboard')

        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_function

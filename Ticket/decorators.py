from User.models import Admin
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


@login_required()
def admin_login_required(func):
    def wrapper(request):
        if Admin.objects.filter(user=request.user).count() == 0:
            return HttpResponseForbidden('You think you are admin?! Dream on!')
        return func
    return wrapper
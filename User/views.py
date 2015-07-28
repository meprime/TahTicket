from django.shortcuts import render
from Ticket.forms import *


def user_profile(request):
    user_update_form = UserUpdateForm
    return render(request, 'user_profile.html', {
        'user_update_form': user_update_form,
    })
from django.shortcuts import render
from Ticket.forms import *
from User.models import *
from Event.models import BoughtTicket
from Ticket.decorators import user_login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponseForbidden


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if Admin.objects.filter(user=user).count():
                print('admin logged in')
                return HttpResponseRedirect('/management/')
            else:
                print('ordinary user logged in')
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def sign_out(request):
    logout(request)
    return HttpResponseRedirect("/")


def sign_up(request):
    login_form = LoginForm()
    user_form = UserRegistrationForm()
    userprofile_form = UserProfileRegistrationForm()
    success_msg = ''
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        userprofile_form = UserProfileRegistrationForm(request.POST)
        if user_form.is_valid() and userprofile_form.is_valid():
            # CHECK WHETHER THE PASSWORD AND ITS CONFIRMATION MATCH
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            userprofile = userprofile_form.save(commit=False)
            userprofile.user = user
            userprofile.save()
            success_msg = 'ثبت‌نام شما با موفقیت انجام شد'
    else:
        pass
    return render(request, 'sign_up_in.html', {
        'login_form': login_form,
        'user_form': user_form,
        'userprofile_form': userprofile_form,
        'success_message': success_msg,
    })


@user_login_required(login_url='/')
def user_profile(request):
    user = request.user
    user_update_form = UserUpdateForm(
        initial={
            'nl_memb': user.userprofile.nl_memb,
        }
    )
    if request.method == 'POST':
        pass
    return render(request, 'user_profile.html', {
        'user_update_form': user_update_form,
        'userprofile': user.userprofile,
    })


@user_login_required(login_url='/')
def user_tickets(request):
    user = request.user
    return render(request, 'user_tickets.html', {
        'bought_tickets': BoughtTicket.objects.filter(buyer=user.userprofile),
        'login_form': LoginForm()
    })

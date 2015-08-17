from django.shortcuts import render
from Ticket.forms import *
from User.models import *
from Event.models import BoughtTicket
from django.core.mail import send_mail
from Ticket.decorators import user_login_required
from django.contrib.auth.decorators import login_required
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


@login_required(login_url='/')
def user_profile(request):
    user = request.user
    success_msg = ''
    if Admin.objects.filter(user=user).count() == 0:  #user is not admin
        user_update_form = UserUpdateForm(
            initial={
                'nl_memb': user.userprofile.nl_memb,
            }
        )
    else:  #user is admin
        user_update_form = UserUpdateForm()
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST)
        if user_update_form.is_valid():
            user.set_password(user_update_form.cleaned_data['password'])
            user.save()
            if Admin.objects.filter(user=user).count() == 0:  #user is not admin
                user.userprofile.nl_memb = user_update_form.cleaned_data['nl_memb']
                user.userprofile.save()
            success_msg = 'تغییرات با موفقیت انجام شد'

    is_admin = False
    if Admin.objects.filter(user=user).count() > 0:
        is_admin = True
    return render(request, 'user_profile.html', {
        'user_update_form': user_update_form,
        'user': user,
        'success_message': success_msg,
        'is_admin': is_admin,
    })


@user_login_required(login_url='/')
def user_tickets(request):
    user = request.user
    return render(request, 'user_tickets.html', {
        'bought_tickets': BoughtTicket.objects.filter(buyer=user.userprofile),
        'login_form': LoginForm()
    })


def forgot_password(request):
    error_msg = ''
    success_msg = ''
    if request.method == 'POST':
        print('method is post')
        email = request.POST['email']
        users = User.objects.filter(email=email)
        if users:
            print("say hi")
            user = users[0]     #assuming email is unique
            pw = User.objects.make_random_password()
            user.set_password(pw)
            user.save()
            send_mail('TahTicket password reset', pw, 'password_reset@popcorn.com', [email])
            success_msg = 'ایمیلی جهت بازیابی رمز عبورتان برایتان ارسال شده‌است '
        else:
            print("say bye")
            error_msg = 'ایمیلتان معتبر نیست'

    #form = ForgotPasswordForm

    return render(request, "forgot_password.html", {
        #'form': form,
        'error_message': error_msg,
        'success_message': success_msg,
        })

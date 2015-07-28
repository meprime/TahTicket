from django.shortcuts import render
from Ticket.forms import ForgotPasswordForm

def index(request):
    return render(request, 'index.html')


def contact_us(request):
    return render(request, 'contact.html')


def user_tickets(request):
    return render(request, 'user_tickets.html')


def organizer_all_events(request):
    return render(request, 'organizer_events_list.html')


def search(request):
    return render(request, 'shop.html')


def checkout(request):
    return render(request, 'checkout.html')


def bank(request):
    return render(request, 'fake_bank.html')


def code(request):
    return render(request, 'code.html')


def forgot_password(request):
    form = ForgotPasswordForm()
    return render(request, 'forgot_password.html', {
        'form': form,
    })


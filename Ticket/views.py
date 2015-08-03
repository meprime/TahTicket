from django.shortcuts import render

from Event.models import *
from User.models import *
from django.contrib.auth import authenticate, login, logout
from Ticket.forms import ForgotPasswordForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if Admin.objects.filter(user=user).count():  # logging admin in
                login(request, user)
                print('admin logged in')
                return HttpResponseRedirect('/management/')
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def sign_out(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required(login_url='/')
def admin(request):
    if Admin.objects.filter(user=request.user).count() == 0:
        # SHOULD ACTUALLY BE DONE WITH A DECORATOR, BUT... :-|
        return HttpResponseForbidden('You think you are admin?! Dream on!')

    return render(request, 'admin.html')


def index(request):
    types = Type.objects.all()
    images = []
    for i in range(1, types.__sizeof__()):
        images += "images/type/" + i.__str__() + ".jpg"
    events = Event.objects.all()
    new_events = []
    for i in range(0, 4):
        if events.__len__() >= i:
            new_events.append(events[i])

    tickets = Ticket.objects.all().order_by('sold')
    top_events = []
    for i in range(0, 3):
        if tickets.__len__() >= i:
            top_events.append(tickets[i].event)

    subtypes = SubType.objects.all()
    return render(request, 'index.html',
                  {
                      "types": types,
                      "images": images,
                      "subtypes": subtypes,
                      "new_events": new_events,
                      "top_events": top_events,
                      'login_form': LoginForm(),  # ADDED BY SADRA
                  })


def contact_us(request):
    return render(request, 'contact.html')


def user_tickets(request):
    return render(request, 'user_tickets.html')


@login_required(login_url='/')
def admin_all_events(request):
    all_events = Event.objects.all()
    events = []
    for event in all_events:
        tickets = Ticket.objects.filter(event=event)
        sold_tickets = BoughtTicket.objects.filter(ticket__in=tickets)
        tickets_price = 0
        for t in sold_tickets:
            tickets_price += t.ticket.price
        e = {
            'title': event.title,
            'date': event.date,
            'type': event.type,
            'sub_type': event.sub_type,
            'id': event.id,
            'sold_tickets': sold_tickets.count(),
            'tickets_price': tickets_price,
        }
        events.append(e)

    return render(request, 'organizer_events_list.html', {
        'events': events,
    })


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


def type_view(request, type_id):
    return render(request, 'contact.html')

def event_view(request, event_id):
    return render(request, 'details.html')

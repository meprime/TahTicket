from django.shortcuts import render

import datetime
from Event.models import *
from User.models import *
from django.contrib.auth import authenticate, login, logout
from Ticket.forms import ForgotPasswordForm, LoginForm, DateForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseForbidden


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
    events = Event.objects.all().order_by("-id")
    new_events = []
    for i in range(0, 4):
        if events.__len__() >= i:
            new_events.append(events[i])
            print(events[i].title)

    tickets = Ticket.objects.all().order_by("-sold")
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
    return render(request, 'contact.html', {'login_form': LoginForm()})


def user_tickets(request):
    return render(request, 'user_tickets.html', {'login_form': LoginForm()})


@login_required(login_url='/')
def admin_all_events(request):
    all_events = Event.objects.all()

    if request.method == 'POST':
        from_date = request.POST.get('from-date', None)
        to_date = request.POST.get('to-date', None)
        if from_date and to_date:
            d1 = from_date.split('/')
            d2 = to_date.split('/')
            d1 = datetime.date(int(d1[2]), int(d1[0]), int(d1[1]))
            d2 = datetime.date(int(d2[2]), int(d2[0]), int(d2[1]))
            all_events = Event.objects.filter(date__lte=d2).filter(date__gte=d1)

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
            'login_form': LoginForm()
        }
        events.append(e)

    return render(request, 'organizer_events_list.html', {
        'events': events,
        'login_form': LoginForm(),
        'from_date_form': DateForm(),
        'to_date_form': DateForm(),
    })


def search(request):
    return render(request, 'shop.html', {'login_form': LoginForm()})


def checkout(request):
    return render(request, 'checkout.html', {'login_form': LoginForm()})


def bank(request):
    return render(request, 'fake_bank.html', {'login_form': LoginForm()})


def code(request):
    return render(request, 'code.html', {'login_form': LoginForm()})


def forgot_password(request):
    form = ForgotPasswordForm()
    return render(request, 'forgot_password.html', {
        'form': form,
        'login_form': LoginForm()
    })


def event_view(request, event_id):
    return render(request, 'details.html', {'login_form': LoginForm()})


def test_view(request):
    return render(request, 'Type.html', {'login_form': LoginForm()})


def type_view(request, type_id):
    types = Type.objects.all()
    subtypes = SubType.objects.all()
    c_type = Type.objects.filter(id=type_id)[0]
    events = Event.objects.filter(type=c_type)
    c_subtypes = SubType.objects.filter(type=c_type)
    print(c_type)
    print(events)
    return render(request, 'Type.html', {
        "subtypes": subtypes,
        "types": types,
        "c_type": c_type,
        "c_subtypes": c_subtypes,
        'login_form': LoginForm(),
        'events': events
        })


def type_type_view(request, type_id, subtype_id):
    types = Type.objects.all()
    subtypes = SubType.objects.all()
    return render(request, 'contact.html', {
        "subtypes": subtypes,
        "types": types,
        'login_form': LoginForm()
    })

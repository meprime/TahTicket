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
    query = request.GET.get('q')
    stype = request.GET.get('stype')
    price = request.GET.get('price')
    result = Event.objects.all()
    st_val = 0
    t_val = 0

    if stype is not None and stype != "0-0":
        print("TYPE" + stype)
        tmp = stype.split("-")
        t_val = int(tmp[0])
        if tmp[1] != "0":
            subtype_list = SubType.objects.filter(id=tmp[1])
            if subtype_list is not None and subtype_list.__len__() > 0:
                result = result.filter(sub_type=subtype_list[0])
                st_val = int(tmp[1])
        else:
            type_list = Type.objects.filter(id=tmp[0])
            if type_list is not None and type_list.__len__() > 0:
                result = result.filter(type=type_list[0])
            st_val = 0
    if price is not None:
        prices = price.split("%2C")
        low_price = prices[0]
        high_price = prices[1]
        print(low_price)
        print(high_price)

    if query is not None and query != "":
        result = process_query_users(query, result)
    else:
        query = ""

    empty = 0
    if result.__len__() == 0:
        empty = 1

    types = Type.objects.all()
    subtypes = SubType.objects.all()
    print(subtypes)

    return render(request, 'shop.html', {
        "empty": empty,
        "query": query,
        "type": t_val,
        "stype": st_val,
        "subtypes": subtypes,
        "types": types,
        'result': result,
        'login_form': LoginForm()
    })


def process_query_users(query, result):
    results = []
    temp = query.split('+')
    terms = []
    print(temp)
    for term in temp:
        print(term + "1")
        terms += term.split(' ')
    for term in terms:
        print(term)
        results += result.filter(title__contains=term)
    return results


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
    empty = 0
    if events.__len__() == 0:
        empty = 1
    return render(request, 'Type.html', {
        "empty": empty,
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
    subtype = SubType.objects.filter(id=subtype_id)[0]
    events = Event.objects.filter(sub_type=subtype)
    type = Type.objects.filter(id=type_id)[0]
    empty = 0
    if events.__len__() == 0:
        empty = 1
    return render(request, 'subtype.html', {
        "empty": empty,
        "subtypes": subtypes,
        "types": types,
        "c_subtype": subtype,
        "c_type": type,
        "events": events,
        'login_form': LoginForm()
    })

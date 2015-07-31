from django.shortcuts import render

from Event.models import *
from Ticket.forms import ForgotPasswordForm


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
                  })


def contact_us(request):
    return render(request, 'contact.html')


def user_tickets(request):
    return render(request, 'user_tickets.html')


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


def type(request, type_id):
    render(request, 'contact.html')

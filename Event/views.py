# coding=utf-8
from django.shortcuts import render
from Ticket.forms import *
from django.http import HttpResponseRedirect, Http404


def admin_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
    except:
        return Http404('رویداد مورد نظرتان وجود ندارد.')

    if request.method == 'POST':
        if 'update-event' in request.POST:
            event_form = UpdateEventForm(request.POST or None, instance=event)
            if event_form.is_valid():
                event_form.save()
        if 'add-ticket' in request.POST:
            ticket_form = NewTicketTypeForm(request.POST)
            if ticket_form.is_valid():
                new_ticket = ticket_form.save(commit=False)
                new_ticket.event = event
                new_ticket.save()

    ticket_form = NewTicketTypeForm
    update_event_form = UpdateEventForm(  # needs to be taken care of
        initial={
            'description': event.description,
            'date': event.date,
            'time': event.time,
            'venue': event.venue,
            }
    )
    ticket_types = Ticket.objects.filter(event=event)
    tickets = []
    for tt in ticket_types:
        tickets.append({
            'type': tt.type,
            'capacity': tt.capacity,
            'sold': tt.sold,
        })

    return render(request, 'organizer_event.html', {
        'event': event,
        'tickets': tickets,
        'ticket_form': ticket_form,
        'update_event_form': update_event_form,
    })


def new_event(request):
    event_form = NewEventForm
    venue_form = NewVenueForm
    success_msg = ''
    error_msg = ''
    if request.method == 'POST':
        if 'new-event' in request.POST:
            event_form = NewEventForm(request.POST)
            if event_form.is_valid():
                new_event = event_form.save()
                success_msg = 'رویداد جدید با موفقیت اضافه شد'
        if 'new-venue' in request.POST:
            venue_form = NewVenueForm(request.POST)
            if venue_form.is_valid():
                new_venue = venue_form.save()
                success_msg = 'مکان جدید با موفقیت اضافه شد'
    return render(request, 'new_event.html', {
        'event_form': event_form,
        'venue_form': venue_form,
        'success_message': success_msg,
        'error_message': error_msg,
    })


def remove_event(request, event_id):
    try:
        Event.objects.get(id=event_id).delete()
    except:
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def show_ticket(request):
    return render(request, 'ticket.html')


def details(request):
    return render(request, 'details.html')


def concert(request):
    return render(request, 'concert.html')


def classic(request):
    return render(request, 'classic.html')

def details2(request):
    return render(request, 'details2.html')

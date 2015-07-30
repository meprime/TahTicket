# coding=utf-8
from django.shortcuts import render
from Ticket.forms import *
from django.http import HttpResponseRedirect


def organizer_event(request):
    ticket_form = NewTicketTypeForm
    update_event_form = UpdateEventForm(  # needs to be taken care of
        initial={
            'description': 'یک مسابقه‌ی هیجان‌انگیز',
            }
    )
    return render(request, 'organizer_event.html', {
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

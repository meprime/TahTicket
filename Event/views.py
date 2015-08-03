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


def admin_types(request):
    type_form = TypeForm
    subtype_form = SubTypeForm
    success_msg = ''
    error_msg = ''
    if request.method == 'POST':
        if 'new-type' in request.POST:
            type_form = TypeForm(request.POST)
            if type_form.is_valid():
                type_form.save()
                success_msg = 'دسته‌ی جدید با موفقیت اضافه شد'
        if 'new-subtype' in request.POST:
            subtype_form = SubTypeForm(request.POST)
            if subtype_form.is_valid():
                subtype_form.save()
                success_msg = 'زیردسته‌ی جدید با موفقیت اضافه شد'

    types = Type.objects.all()
    types_subtypes = []
    for type in types:
        s = SubType.objects.filter(type=type)
        types_subtypes.append({
            'name': type.name,
            'id': type.id,
            'subtypes': SubType.objects.filter(type=type),
        })

    return render(request, 'admin_types.html', {
        'type_form': type_form,
        'subtype_form': subtype_form,
        'types': types_subtypes,
        'success_message': success_msg,
        'error_message': error_msg,
    })


def remove_type(request, type_id):
    try:
        type = Type.objects.get(id=type_id)
        if Event.objects.filter(type=type).count() == 0:
            type.delete()
        else:
            pass  # better send an error message
    except:
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_subtype(request, subtype_id):
    try:
        subtype = SubType.objects.get(id=subtype_id)
        if Event.objects.filter(sub_type=subtype).count() == 0:
            type.delete()
        else:
            pass  # better send an error message
    except:
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def show_ticket(request):
    return render(request, 'ticket.html')


def details(request):
    return render(request, 'details.html')


def details2(request):
    return render(request, 'details2.html')

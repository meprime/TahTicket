from django.contrib import admin
from .models import *


class EventAdmin(admin.ModelAdmin):
    exclude = ()
    list_display = ('title', 'date', 'sold_tickets', 'tickets_price_sum',)
    search_fields = ['date']

    def sold_tickets(self, obj):
        tickets = Ticket.objects.filter(event=obj)
        return BoughtTicket.objects.filter(ticket__in=tickets).count()

    def tickets_price_sum(self, obj):
        tickets = Ticket.objects.filter(event=obj)
        btickets = BoughtTicket.objects.filter(ticket__in=tickets)
        s = 0
        for t in btickets:
            s += t.ticket.price
        return s


admin.site.register(Event, EventAdmin)
#admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(BoughtTicket)
admin.site.register(Type)
admin.site.register(SubType)
admin.site.register(Venue)

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Ticket.views.index'),
    url(r'^contact/$', 'Ticket.views.contact_us'),
    url(r'^event/', 'Event.views.single_event'),
    url(r'^organizer-event/', 'Event.views.organizer_event'),  # LATER COULD BE MERGED WITH EVENT
    url(r'^new-event/', 'Event.views.new_event'),
    url(r'^ticket/', 'Event.views.show_ticket'),
    url(r'^my-events/', 'Ticket.views.organizer_all_events'),
    url(r'^my-tickets/', 'Ticket.views.user_tickets'),
    url(r'^checkout/', 'Ticket.views.checkout'),
    url(r'^user-profile/', 'User.views.user_profile'),
    url(r'^search/', 'Ticket.views.search'),
    url(r'^details/$', 'Event.views.details'),
    url(r'^details2/$', 'Event.views.details2'),
    url(r'^concert/$', 'Event.views.concert'),
    url(r'^concert/classic/$', 'Event.views.classic'),
    url(r'^fake_bank$', 'Ticket.views.bank'),
    url(r'^code$', 'Ticket.views.code'),
    url(r'^forgot-password/', 'Ticket.views.forgot_password'),

]

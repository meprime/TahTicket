from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^management/$', 'Ticket.views.admin'),
    url(r'^$', 'Ticket.views.index'),
    url(r'^sign-up/$', 'User.views.sign_up'),
    url(r'^login/$', 'User.views.sign_in'),
    url(r'^logout/$', 'User.views.sign_out'),
    url(r'^contact/$', 'Ticket.views.contact_us'),
    url(r'^admin-event/(?P<event_id>[a-zA-Z0-9]*)/$', 'Event.views.admin_event'),  # LATER COULD BE MERGED WITH EVENT
    url(r'^new-event/', 'Event.views.new_event'),
    url(r'^remove-event/(?P<event_id>[a-zA-Z0-9]*)/$', 'Event.views.remove_event'),
    url(r'^upload-poster/(?P<event_id>[a-zA-Z0-9]*)/$', 'Event.views.upload_poster'),
    url(r'^types/', 'Event.views.admin_types'),
    url(r'^remove-type/(?P<type_id>[a-zA-Z0-9]*)/$', 'Event.views.remove_type'),
    url(r'^remove-subtype/(?P<subtype_id>[a-zA-Z0-9]*)/$', 'Event.views.remove_subtype'),
    url(r'^ticket/(?P<ticket_id>[a-zA-Z0-9]*)/$', 'Event.views.show_ticket'),
    url(r'^all-events/', 'Ticket.views.admin_all_events'),
    url(r'^checkout/', 'Ticket.views.checkout', name='checkout'),
    url(r'^my-tickets/', 'User.views.user_tickets'),
    url(r'^user-profile/', 'User.views.user_profile'),
    url(r'^search/', 'Ticket.views.search'),
    url(r'^details/$', 'Event.views.details', name='details'),
    url(r'^details2/$', 'Event.views.details2'),
    url(r'^type/(?P<type_id>\d+)$', 'Ticket.views.type_view'),
    url(r'^type/(?P<type_id>\d+)/(?P<subtype_id>\d+)$', 'Ticket.views.type_type_view'),
    url(r'^fake_bank$', 'Ticket.views.bank'),
    url(r'^code$', 'Ticket.views.code'),
    url(r'^event/(?P<event_id>\d+)$', 'Ticket.views.event_view'),
    url(r'buy/(?P<event_id>\d+)$', 'Ticket.views.buy_view'),
    url(r'^favorite/(?P<event_id>\d+)$', 'Ticket.views.add_to_favorites'),
    url(r'^rate/(?P<event_id>\d+)$', 'Ticket.views.rate'),
    url(r'^forgot-password/', 'User.views.forgot_password'),
    url(r'^test/', 'Ticket.views.test_view'),

]

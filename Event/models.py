from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now

from User.models import EventOrganizer, Customer


class Venue(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=80)
    # decompose address as city, street, number

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class SubType(models.Model):
    name = models.CharField(max_length=40)
    type = models.ForeignKey(Type)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    date = models.DateField(default=now().date())
    time = models.TimeField(default=now().time())
    # img =
    venue = models.ForeignKey(Venue)
    type = models.ForeignKey(Type)
    sub_type = models.ForeignKey(SubType)
    organizer = models.ForeignKey(EventOrganizer)

    '''
    def clean(self):
        super(self)
        if SubType.objects.get(id=self.sub_type).type_id != self.type:
            raise ValidationError('sub_type should actually be a sub-type of type!')
    '''

    def __str__(self):
        return self.title


class Ticket(models.Model):
    event = models.ForeignKey(Event)
    type = models.CharField(max_length=20)
    capacity = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)
    price = models.IntegerField(default=0)


class BoughtTicket(models.Model):
    ticket = models.ForeignKey(Ticket)
    buyer = models.ForeignKey(Customer)
    serial_no = models.BigIntegerField(null=True, blank=True)



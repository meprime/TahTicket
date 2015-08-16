from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from datetime import date, time, datetime
from User.models import UserProfile


class Venue(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=80)
    # decompose address as city, street, number

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name + " - " + self.description


class SubType(models.Model):
    name = models.CharField(max_length=40)
    type = models.ForeignKey(Type)

    def __str__(self):
        return self.type.name + ' - ' + self.name


class Event(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    date = models.DateField(default=date.today, blank=True)
    time = models.TimeField(default=now().time(), blank=True)
    venue = models.ForeignKey(Venue)
    type = models.ForeignKey(Type, default=1)
    sub_type = models.ForeignKey(SubType)
    rate = models.ManyToManyField(UserProfile, through="TicketRate")
    favorites = models.ManyToManyField(UserProfile, related_name="favorites")

    '''
    def clean(self):
        super(self)
        if SubType.objects.get(id=self.sub_type).type_id != self.type:
            raise ValidationError('sub_type should actually be a sub-type of type!')
    '''
    def __lt__(self, other):
        self_rates = TicketRate.objects.filter(event=self)
        other_rates = TicketRate.objects.filter(event=other)
        if self_rates.__len__() == 0:
            return True
        elif other_rates.__len__() == 0:
            return False
        else:
            self_avg = sum(r.rate for r in self_rates) / self_rates.count()
            other_avg = sum(r.rate for r in other_rates) / other_rates.count()
            if self_avg <= other_avg:
                return True
            else:
                return False

    def __str__(self):
        return self.title


class TicketRate(models.Model):
    user = models.ForeignKey(UserProfile)
    event = models.ForeignKey(Event)
    rate = models.IntegerField(default=0)


class Ticket(models.Model):
    event = models.ForeignKey(Event)
    type = models.CharField(max_length=20)
    capacity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)


class BoughtTicket(models.Model):
    ticket = models.ForeignKey(Ticket)
    buyer = models.ForeignKey(UserProfile)
    date = models.DateField(default=date.today, blank=True)
    serial_no = models.BigIntegerField(null=True, blank=True)



# coding=utf-8
from django import forms
from django.forms import Textarea
from Ticket.models import ContactMessage
from django.contrib.auth.models import User
from User.models import UserProfile
from Event.models import Event, Venue, Ticket, Type, SubType
from django.utils.translation import ugettext_lazy as _


class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['organizer']

        labels = {
            'title': _('عنوان'),
            'description': _('توضیحات'),
            'date': _('تاریخ'),
            'time': _('زمان'),
            'venue': _('مکان'),
            'type': _('دسته'),
            'sub_type': _('زیردسته'),
        }
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),
            'description': Textarea(attrs={'cols': 40, 'rows': 2}),
        }


class UpdateEventForm(forms.ModelForm):  # used for organizer to update some properties of her event
    class Meta:
        model = Event
        fields = ['description', 'date', 'time', 'venue']
        labels = {
            'description': _('توضیحات'),
            'date': _('تاریخ'),
            'time': _('زمان'),
            'venue': _('مکان'),
        }
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker'}),
            'description': Textarea(attrs={'cols': 40, 'rows': 2}),
        }


class NewVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        exclude = []
        labels = {
            'name': _('نام'),
            'address': _('آدرس'),
        }


class NewTicketTypeForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['event', 'sold']
        labels = {
            'type': _('نوع'),
            'capacity': _('ظرفیت'),
            'price': _('قیمت'),
        }


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='تأیید رمز عبور')
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        labels = {
            'username': _('نام کاربری'),
            'password': _('رمز عبور'),
            'email': _('ایمیل'),
        }


class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_no', 'gender']
        labels = {
            'phone_no': _('شماره‌ی تماس'),
            'gender': _('جنسیت'),
        }


class UserUpdateForm(forms.Form):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(), required=True, label='رمز عبور جدید')
    confirm_password = forms.CharField(max_length=50, widget=forms.PasswordInput(), required=True, label='تأیید رمز عبور')
    nl_memb = forms.BooleanField(label='عضویت در خبرنامه')  #newsletter membership


class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        exclude = []
        labels = {
            'name': 'نام دسته',
            'description': 'توضیح دسته',
        }
        widgets = {
            'description': Textarea(attrs={'cols': 40, 'rows': 2}),
        }


class SubTypeForm(forms.ModelForm):
    class Meta:
        model = SubType
        exclude = []
        labels = {
            'name': 'نام زیردسته',
            'type': 'دسته',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        exclude = []


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'نام کاربری',
            'password': 'رمز عبور',
        }
        widgets = {
            'password': forms.PasswordInput()
        }


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()


class UploadImageForm(forms.Form):
    image = forms.ImageField()

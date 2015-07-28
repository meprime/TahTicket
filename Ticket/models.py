from django.db import models
from Event.models import Event
from User.models import UserProfile


class Comment(models.Model):
    commenter = models.ForeignKey(UserProfile)
    event = models.ForeignKey(Event)
    text = models.TextField()


class CommentResponse(models.Model):
    responder = models.ForeignKey(UserProfile)
    text = models.TextField()


class ContactMessage(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=11, blank=True, null=True)
    text = models.TextField()

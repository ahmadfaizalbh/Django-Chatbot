from django.db import models

# Create your models here.


class Sender(models.Model):
    messengerSenderID = models.TextField()
    topic = models.TextField()


class Memory(models.Model):
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    key = models.TextField()
    value = models.TextField()


class Conversation(models.Model):
    sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    bot = models.BooleanField(default=True)

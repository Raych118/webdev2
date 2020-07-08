from django.db import models
from django.core.validators import RegexValidator
import random


class Pull(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    number = models.CharField(max_length=20, blank=True, validators=[alphanumeric])


class Enquiry(models.Model):
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    customer_name = models.CharField(max_length=30)
    number = models.CharField(max_length=20, blank=True, validators=[alphanumeric])
    email = models.EmailField()
    question = models.TextField()
    reply = models.TextField(default=None, null=True)
    replied = models.BooleanField(default=False)
    id = random.randrange(0, 1000000)

    def __str__(self):
        if self.replied:
            string = self.customer_name + "-" + " replied"
        else:
            string = self.customer_name + "-" + " pending"
        return string

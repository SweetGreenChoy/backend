from django.db import models

# Create your models here.
class Seat(models.Model):

    seat_number = models.IntegerField(unique=True)
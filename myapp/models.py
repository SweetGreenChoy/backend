from django.db import models
import uuid

# Create your models here.
class Seat(models.Model):

    ticket_key = models.UUIDField(default=uuid.uuid4)
    seat_number = models.IntegerField(unique=True)
    customer_name = models.CharField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
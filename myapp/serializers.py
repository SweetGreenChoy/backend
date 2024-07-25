from rest_framework import serializers
from .models import Seat

class SeatSerializer(serializers.ModelSerializer):
    
    class Meta:

        model = Seat
        fields = ['seat_number', 'customer_name']
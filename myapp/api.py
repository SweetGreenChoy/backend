from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

class SeatList(APIView):

    def get(self, request):

        model = Seat.objects.all()
        serializer = SeatSerializer(model, many=True)
        return Response(serializer.data)
    
    def post(self, request):

        serializer = SeatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
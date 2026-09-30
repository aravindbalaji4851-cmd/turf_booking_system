from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from slot_booking.models import Booking
from slot_booking.serializer import BookingSerializer
# Create your views here.

class BookingCreateListView(APIView):

    def get(self,request):

        qs = Booking.objects.all()

        serializer_inst = BookingSerializer(qs,many=True)

        return Response(data=serializer_inst.data)
    


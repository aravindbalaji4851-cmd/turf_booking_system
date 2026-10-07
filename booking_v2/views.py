from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from booking_v2.serializers import SignUpSerializer,BookingSerializer
from booking_v2.models import Slots

from datetime import timedelta,datetime,time

# Create your views here.

class SignUpView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_inst = SignUpSerializer(data = form_data)

        if serializer_inst.is_valid():

            cleaned_data = serializer_inst.validated_data

            user_object = User.objects.create_user(**cleaned_data)
            
            serial_inst = SignUpSerializer(user_object)

            return Response(data=serial_inst.data)

        else: return Response(data=serializer_inst.errors)


class BookingCreateListView(APIView):

    def get(self,request):

        qs = Slots.objects.all()

        serializer_inst = BookingSerializer(qs,many=True)

        return Response(data=serializer_inst.data)

    def post(self,request):

        form_data = request.data

        serializer_inst = BookingSerializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data = serializer_inst.validated_data

            turf = cleaned_data.get("turf")

            cleaned_data = serializer_inst.validated_data

            booking_date = cleaned_data.get("booking_date")
            
            start_time = cleaned_data.get("start_time")

            duration = cleaned_data.get("duration")

            end_date_time = datetime.combine(booking_date,start_time) + timedelta(hours=duration)

            end_time = end_date_time.time()

            matching_booking = Slots.objects.filter(turf=turf,booking_date=booking_date,start_time__lt=end_time,end_time__gt=start_time).exists()

            if matching_booking:   

                return Response({"Sorry, slot already booked"})

            else:

                cleaned_data["end_time"] = end_time

                qs = Slots.objects.create(**cleaned_data)

                serial_inst = BookingSerializer(qs)

                return Response(data=serial_inst.data)

        else: return Response(serializer_inst.errors)

        

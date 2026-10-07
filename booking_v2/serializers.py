from django.contrib.auth.models import User

from rest_framework import serializers

from booking_v2.models import Slots

from datetime import date

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ["username","email","password"]

class BookingSerializer(serializers.ModelSerializer):

    class Meta:

        model = Slots

        fields = "__all__"

        read_only_fields = ["id","end_time"]


    def validate(self,validated_data):

        booking_date = validated_data.get("booking_date")

        if booking_date < date.today():

            raise serializers.ValidationError("invalid date")

        else: return validated_data
        
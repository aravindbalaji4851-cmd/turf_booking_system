from django.contrib.auth.models import User

from rest_framework import serializers

from booking_v2.models import Slots

from datetime import date,timedelta

class SignUpSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ["username","email","password"]

class BookingSerializer(serializers.ModelSerializer):

    turf = serializers.StringRelatedField()

    class Meta:

        model = Slots

        fields = "__all__"

        read_only_fields = ["id","end_time"]


    def validate(self,validated_data):

        booking_date = validated_data.get("booking_date")
        duration = validated_data.get("duration")

        if booking_date < date.today():

            raise serializers.ValidationError("invalid date")

        if duration < timedelta(hours=1): 

            raise serializers.ValidationError("minimum duration is 1 hr")

        return validated_data        
        
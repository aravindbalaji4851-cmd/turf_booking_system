from rest_framework import serializers

class BookingSerializer(serializers.Serializer):

    customer_name = serializers.CharField()

    turf = serializers.IntegerField()

    booking_data = serializers.DateField()

    booking_time = serializers.TimeField()

    duration = serializers.IntegerField()

    phone_number = serializers.IntegerField()

    email = serializers.EmailField()


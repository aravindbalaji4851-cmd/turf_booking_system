from rest_framework import serializers


class UserSerializer(serializers.Serializer):

    username = serializers.CharField()

    email = serializers.EmailField()

    password = serializers.CharField()

class TurfSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    name = serializers.CharField()

    location = serializers.CharField()

    phone = serializers.IntegerField()

    fee = serializers.IntegerField()
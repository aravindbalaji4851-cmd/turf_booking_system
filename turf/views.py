from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from turf.serializers import UserSerializer,TurfSerializer
from turf.models import Turf
# Create your views here.

class UserCreateView(APIView):


    def post(self,request):

        form_data = request.data

        serializer_inst = UserSerializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data = serializer_inst.validated_data

            User.objects.create_superuser(**cleaned_data)

            return Response(data=serializer_inst.validated_data)

        else: return Response(data=serializer_inst.errors)

class TurfCreateListView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self,request):

        qs = Turf.objects.all()

        serializer_inst = TurfSerializer(qs,many=True)

        return Response(data=serializer_inst.data)

    def post(self,request):

        form_data = request.data

        serializer_inst = TurfSerializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data = serializer_inst.validated_data

            Turf.objects.create(**cleaned_data)

            return Response(serializer_inst.validated_data)

        else: return Response(data=serializer_inst.errors)

class TurfRetrieveUpdate(APIView):

    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def get(self,request,pk=None):

        qs = Turf.objects.get(id=pk)

        serializer_inst = TurfSerializer(qs)

        return Response(data = serializer_inst.data)

    def put(self,request,pk=None):

        form_data = request.data

        serializer_inst = TurfSerializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data = serializer_inst.validated_data

            Turf.objects.filter(id=pk).update(**cleaned_data)

            return Response(data=serializer_inst.validated_data)

        else: return Response(data=serializer_inst.errors)

    
    

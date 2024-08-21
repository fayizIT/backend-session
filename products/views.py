from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import AddCampSerializers
from rest_framework.response import Response
from rest_framework import status


class AddCamp(APIView):
    def post(self,request):
        try:
            camp_admin = request.user
            data = request.data.copy()
            data["camp_create_by"] = camp_admin.id
            serializer = AddCampSerializers(data)
            if serializer.data_is_Valid():
                serializer.save()   
                return Response(serializer.data,status=status.status.HTTP_201_CREATED)
            
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
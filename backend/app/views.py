from django.views.generic.base import TemplateView
from django.views import View
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.views.generic.list import ListView

from .models import CustomUser
from .serializer import UserSerializer

import datetime

class UserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class SampleAPIView(APIView):
    def get(self, request):
        return Response("OK", status=status.HTTP_200_OK)


class DateTimeView(APIView):
    def get(self, request):
        datetime_str = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        return Response(datetime_str, status=status.HTTP_200_OK)


class IndexView(TemplateView):
    template_name = "index.html"
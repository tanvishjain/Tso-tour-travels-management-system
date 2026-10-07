from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.
class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = stateSerializer

class cityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = citySerializer
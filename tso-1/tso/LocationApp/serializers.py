from rest_framework import serializers
from .models import *

class stateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class citySerializer(serializers.HyperlinkedModelSerializer):
    State = stateSerializer()
    class Meta:
        model = City
        fields = '__all__'

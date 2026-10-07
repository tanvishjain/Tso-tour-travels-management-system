from rest_framework import serializers
from .models import *
from Account.serializers import *

class contactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class feedbackSerializer(serializers.HyperlinkedModelSerializer):
    User = UserSerializer()
    class Meta:
        model = Feedback
        fields = '__all__'
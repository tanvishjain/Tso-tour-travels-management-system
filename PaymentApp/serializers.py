from rest_framework import serializers
from .models import *
from PackageApp.serializers import bookingSerializer, packageSerializer
from Account.serializers import UserSerializer

class upiSerializer(serializers.HyperlinkedModelSerializer):
    # Booking = bookingSerializer()
    # Package = packageSerializer()
    # User = UserSerializer()
    class Meta:
        model = UPI
        fields = '__all__'

class netbankingSerializer(serializers.HyperlinkedModelSerializer):
    # Booking = bookingSerializer()
    # Package = packageSerializer()
    # User = UserSerializer()
    class Meta:
        model = Net_Banking
        fields = '__all__'

class cardSerializer(serializers.HyperlinkedModelSerializer):
    # Booking = bookingSerializer()
    # Package = packageSerializer()
    # User = UserSerializer()
    class Meta:
        model = Card
        fields = '__all__'

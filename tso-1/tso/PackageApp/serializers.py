from rest_framework import serializers
from .models import *
from LocationApp.models import State
from Account.serializers import *
from LocationApp.serializers import stateSerializer, citySerializer
from EmployeeApp.serializers import guideSerializer, driverSerializer

class packageSerializer(serializers.HyperlinkedModelSerializer):
    State = stateSerializer()
    Guide = guideSerializer()
    class Meta:
        model = Package
        fields = '__all__'

# class discountSerializer(serializers.HyperlinkedModelSerializer):
#     Package = packageSerializer()
#     class Meta:
#         model = Discount
#         fields = '__all__'

class hotelSerializer(serializers.HyperlinkedModelSerializer):
    City = citySerializer()
    class Meta:
        model = Hotel
        fields = '__all__'

class gallerySerializer(serializers.HyperlinkedModelSerializer):
    # User = UserSerializer()
    class Meta:
        model = Gallery
        fields = '__all__'

class bookingSerializer(serializers.HyperlinkedModelSerializer):
    User = UserSerializer()
    Package = packageSerializer()
    class Meta:
        model = Booking
        fields = '__all__'

class cancelSerializer(serializers.HyperlinkedModelSerializer):
    Booking = bookingSerializer()
    class Meta:
        model = Cancellation
        fields = '__all__'

class vehicleSerializer(serializers.HyperlinkedModelSerializer):
    Driver = driverSerializer()
    class Meta:
        model = Vehicle
        fields = '__all__'

class flightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class railSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rail
        fields = '__all__'

class daySerializer(serializers.HyperlinkedModelSerializer):
    Package = packageSerializer()
    City = citySerializer()
    Hotel = hotelSerializer()
    Vehicle = vehicleSerializer()
    Rail = railSerializer()
    Flight = flightSerializer()
    class Meta:
        model = Day_Description
        fields = '__all__'
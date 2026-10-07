from rest_framework import serializers
from .models import *
from LocationApp.models import City
# from PackageApp.serializers import packageSerializer

class guideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'

class driverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class employeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class salarySerializer(serializers.HyperlinkedModelSerializer):
    Guide = guideSerializer()
    Driver = driverSerializer()
    Employee = employeeSerializer()
    # Package = packageSerializer()
    class Meta:
        model = Salary
        fields = '__all__'
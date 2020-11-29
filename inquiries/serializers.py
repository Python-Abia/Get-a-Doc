from rest_framework import serializers
from .models import Syptoms, Inquiry, InquiryCategory
from django.conf import settings

#using the serializer.Serializer class


class SyptomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syptoms
        fields = '__all__'
    
class InquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inquiry
        fields ='__all__'


class InquiryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = InquiryCategory
        fields = '__all__'
        
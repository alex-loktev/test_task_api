from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.ModelSerializer):
    """Customer serializer"""

    class Meta:
        model = Customer
        fields = ('username', 'spent_money', 'deals')


class FileUploadSerializer(serializers.ModelSerializer):
    """File serializer"""

    class Meta:
        model = FileCSV
        fields = ('file',)
from rest_framework import serializers
from .models import Item # Importe o seu modelo Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item 
        fields = '__all__' 
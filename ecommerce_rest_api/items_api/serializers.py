from rest_framework import serializers
from .models import Items

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('id', 'item_category', 'image', 'gender', 'name', 'price', 'tags', 'description', 'clothing_size', 'shoe_size')
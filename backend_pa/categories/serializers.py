from item.serializers import ItemSerializer
from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        items_instance = instance.items.all()
        items_serializer = ItemSerializer(items_instance, many=True)
        representation['items'] = items_serializer.data

        return representation
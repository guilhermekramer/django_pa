from rest_framework import serializers
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

    def create(self, validated_data):
        item = Item.objects.create(
            name=validated_data["name"],
            description=validated_data["description"],
            price=validated_data["price"],
            quantity=validated_data["quantity"],
        )
        return item
    

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     items_instance = instance.items
    #     items_serializer = ItemSerializer(items_instance, many=True)
    #     representation['item'] = items_serializer.data

    #     return representation

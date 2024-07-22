from categories.serializers import CategorySerializer
from rest_framework import serializers

from item.serializers import ItemSerializer
from user.serializers import UserSerializer
from .models import Gasto


class GastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gasto
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        user_instance = instance.user
        user_serializer = UserSerializer(user_instance)
        representation["user"] = user_serializer.data

        Category_instance = instance.category
        Category_serializer = CategorySerializer(Category_instance)
        representation["category"] = Category_serializer.data

        
        # items_instances = instance.items.all()
        # items_serializer = ItemSerializer(items_instances, many=True)
        # representation["items"] = items_serializer.data

        return representation

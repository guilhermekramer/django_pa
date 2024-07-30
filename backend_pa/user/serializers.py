from rest_framework import serializers
from .models import Usuario


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]

    def create(self, validated_data):

        user = Usuario.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
        )

        user.set_password(validated_data["password"])
        user.save()
        return user

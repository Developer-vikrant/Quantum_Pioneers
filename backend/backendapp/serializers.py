from rest_framework import serializers
from django.contrib.auth import get_user_model

User  = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Encrypt password
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class EnquirySerializer(serializers.Serializer):
    name = serializers.CharField()
    mobile_number = serializers.CharField()
    address = serializers.CharField()
    message = serializers.CharField()
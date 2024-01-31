# serializers.py
from rest_framework import serializers
from .models import AppUsers
from django.utils import timezone


class AppUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUsers
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            
        }

    def create(self, validated_data):
        print("Validated Data:", validated_data)
        password = validated_data.pop('password', None)

        # Generate a unique username based on current timestamp
        username = f"user_{int(timezone.now().timestamp())}"

        user = AppUsers.objects.create(username=username, **validated_data)

        if password:
            user.set_password(password)

        user.is_active = False
        user.save()
        return user

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUsers
        fields = ['email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            
        }
       
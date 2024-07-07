from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'username']
        extra_kwargs = {
            'password': {'write_only': True}
        }

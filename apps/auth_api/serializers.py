from django.contrib.auth import get_user_model
from rest_framework import serializers
from .validations import validate_email
# from django.contrib.auth.models import User
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[validate_email])

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password'
        ]

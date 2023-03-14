from rest_framework import serializers

# from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model

# user model
User = get_user_model()


# way one
def validate_email(value):
    user = User.objects.filter(email=value).exists()
    if user:
        raise serializers.ValidationError(
            f"The email:{value} is ALready exists, Use another one")


# unique_user_email = UniqueValidator(queryset=User.objects.all())

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UinqueValidator
from django.contrib.auth.password_validation import validate_password

class registerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        requierd=True,
        validators=[UinqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('id', 'username', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        
        return()
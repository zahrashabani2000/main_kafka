from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
import json

from .serializers import RegisterSerializer
from .producer import ProducerUserCreated


producerUserCreated = ProducerUserCreated()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer()
     
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_extpertion=True)
        self.perform_create(serializer)

        producerUserCreated.publish("user_created_method", json.dumps(serializer.data))
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


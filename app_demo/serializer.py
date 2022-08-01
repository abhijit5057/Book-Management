
from rest_framework import serializers
from app_demo.models import Author
from django.contrib.auth.hashers import make_password
class AuthorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['id','username','email','password']
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(AuthorRegisterSerializer, self).create(validated_data)
        

class AuthorLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = Author
    fields = ['email', 'password']
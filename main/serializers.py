from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User



class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model =Book
        fields ='__all__'


    #Validation on the title
    def validate_title(self,value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty")
        return value
    
    def validate_author(self,value):

        if not value.strip():
            raise serializers.ValidationError("Author must notbbe empty")
        
        return value
    



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
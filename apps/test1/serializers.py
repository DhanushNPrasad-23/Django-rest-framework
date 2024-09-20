from rest_framework import serializers
from .models import Registartion,ItemModel
from django.contrib.auth.models import User




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']
        
    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        
        user = User.objects.create_user(username=username,password=password)
        return user

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source = 'user.username')
    password = serializers.CharField(source = 'user.password')
    
    class Meta:
        model = Registartion
        fields = ['username','password']
        
    def create(self,validated_data):
        user = validated_data.pop('user')
        use = UserSerializer().create(user)
        reg = Registartion.objects.create(user = use)
        return reg
    
    
# =====================================================

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = '__all__'
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class UserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

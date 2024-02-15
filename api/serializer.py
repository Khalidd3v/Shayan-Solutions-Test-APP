from rest_framework import serializers
from .models import Product


#this serializer is made for Product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
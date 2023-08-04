from rest_framework import serializers
from .models import *



class ProductSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = ['title', 'description', 'creation_date', 'picture', 'price', 'category', 'discount', 'supplier']

    def create(self, validated_data):
        create_category = validated_data.pop('category')
        create_discount = validated_data.pop('discount')
        create_supplier = validated_data.pop('supplier')
        product = Product.objects.create(**validated_data)

        for category in create_category:
            Category.objects.create(product=product, **category)

        for discount in create_discount:
            Discount.objects.create(product=product, **discount)

        for supplier in create_supplier:
            Supplier.objects.create(product=product, **supplier)

        return product



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']
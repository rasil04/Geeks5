from rest_framework import serializers
from product.models import Category, Product, Review


#Serializer for Categories list
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

#Serializer for Category
class CategoryRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

#Serialier for Products list
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

#Serializer for Product
class ProductRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

#Serializer for Review list
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

#Serializer for Review
class ReviewRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

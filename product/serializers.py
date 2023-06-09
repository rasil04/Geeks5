from rest_framework import serializers
from product.models import Category, Product, Review


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = 'id name products_count'.split()


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = 'id title description price category_name'.split()


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = 'id text stars product_title'.split()


class ProductsReviewsSerializers(serializers.ModelSerializer):
    review = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = 'id reviews rating'.split()
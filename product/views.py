from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from product.models import Category, Product, Review
from product.serializers import CategorySerializer, ProductSerializer, ReviewSerializer, ProductsReviewsSerializers


@api_view(['GET'])
def categories_list_api_view(request):
    categories = Category.objects.all()
    serializers = CategorySerializer(categories, many=True)
    return Response(data=serializers.data)


@api_view(['GET'])
def categories_detail_api_view(request, id):
    try:
        categorie = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Object not found'})
    serializers = CategorySerializer(categorie)
    return Response(data=serializers.data)


@api_view(['GET'])
def products_list_api_view(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products, many=True)
    return Response(data=serializers.data)


@api_view(['GET'])
def products_detail_api_view(request, id):
    try:
        product1 = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Object not found'})
    serializers = ProductSerializer(product1)
    return Response(data=serializers.data)


@api_view(['GET'])
def reviews_list_api_view(request):
    reviews = Review.objects.all()
    serializers = ReviewSerializer(reviews, many=True)
    return Response(data=serializers.data)


@api_view(['GET'])
def reviews_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Object not found'})
    serializers = ReviewSerializer(review)
    return Response(data=serializers.data)


@api_view(['GET'])
def products_reviews_rating_api_view(request):
    products = Product.objects.all()
    serializer = ProductsReviewsSerializers(products, many=True)
    return Response(data=serializer.data)

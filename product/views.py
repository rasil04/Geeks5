from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from product.models import Category, Product, Review, Tag
from product.serializers import CategorySerializer, ProductSerializer, ReviewSerializer, \
    ProductsReviewsSerializers, ProductValidateSerializers, CategoryValidateSerializers, ReviewValidateSerializers


@api_view(['GET', 'POST'])
def categories_list_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializers = CategorySerializer(categories, many=True)
        return Response(data=serializers.data)
    elif request.method == 'POST':
        serializer = CategoryValidateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get('name')
        category = Category.objects.create(name=name)
        return Response(data=CategorySerializer(category).data)


@api_view(['GET', 'PUT', 'DELETE'])
def categories_detail_api_view(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Object not found'})
    if request.method == 'GET':
        serializers = CategorySerializer(category)
        return Response(data=serializers.data)
    elif request.method == 'PUT':
        serializer = CategoryValidateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        category.name = serializer.validated_data.get('name')
        return Response(data=CategorySerializer(category).data)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def products_list_api_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        return Response(data=serializers.data)
    elif request.method == 'POST':
        serializer = ProductValidateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        price = serializer.validated_data.get('price')
        category = serializer.validated_data.get('category')
        tag = serializer.validated_data.get('tag')
        product = Product.objects.create(title=title, description=description, price=price, tag=tag)
        product.category.set(category)
        product.save()
        return Response(data=ProductSerializer(product).data)


@api_view(['GET', 'PUT', 'DELETE'])
def products_detail_api_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Object not found'})
    if request.method == 'GET':
        serializers = ProductSerializer(product)
        return Response(data=serializers.data)
    elif request.method == 'PUT':
        serializer = ProductValidateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        product.title = serializer.validated_data.get('title')
        product.description = serializer.validated_data.get('description')
        product.price = serializer.validated_data.get('price')
        category = serializer.validated_data.get('category')
        product.category.set(category)
        product.save()
        return Response(data=ProductSerializer(product).data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reviews_list_api_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializers = ReviewSerializer(reviews, many=True)
        return Response(data=serializers.data)
    elif request.method == 'POST':
        serializer = ReviewValidateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        product_id = serializer.validated_data.get('product_id')
        reviews = Review.objects.create(text=text, stars=stars, product_id=product_id)
        return Response(data=ReviewSerializer(reviews).data)


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Object not found'})
    if request.method == 'GET':
        serializers = ReviewSerializer(review)
        return Response(data=serializers.data)
    elif request.method == 'PUT':
        serializer = ReviewValidateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        review.text = serializer.validated_data.get('text')
        review.stars = serializer.validated_data.get('stars')
        review.product_id = serializer.validated_data.get('product_id')
        return Response(data=ReviewSerializer(review).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def products_reviews_api_view(request):
    products = Product.objects.all()
    serializer = ProductsReviewsSerializers(products, many=True)
    return Response(data=serializer.data)

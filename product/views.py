from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from product.models import Category, Product, Review
from product.serializers import CategorySerializer, ProductSerializer, ReviewSerializer, ProductsReviewsSerializers


@api_view(['GET', 'POST'])
def categories_list_api_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializers = CategorySerializer(categories, many=True)
        return Response(data=serializers.data)
    elif request.method == 'POST':
        name = request.data.get('name')
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
        category.name = request.data.get('name')
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
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category = request.data.get('category')
        product = Product.objects.create(title=title, description=description, price=price)
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
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        category = request.data.get('category')
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
        text = request.data.get('text')
        stars = request.data.get('stars')
        product_id = request.data.get('product_id')
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
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.product_id = request.data.get('product_id')
        return Response(data=ReviewSerializer(review).data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def products_reviews_api_view(request):
    products = Product.objects.all()
    serializer = ProductsReviewsSerializers(products, many=True)
    return Response(data=serializer.data)

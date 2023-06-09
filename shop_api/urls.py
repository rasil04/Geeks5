from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from shop_api import settings

from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', views.categories_list_api_view),
    path('api/v1/categories/<int:id>/', views.categories_detail_api_view),
    path('api/v1/products/', views.products_list_api_view),
    path('api/v1/products/<int:id>/', views.products_detail_api_view),
    path('api/v1/reviews/', views.reviews_list_api_view),
    path('api/v1/reviews/<int:id>/', views.reviews_detail_api_view),
    path('api/v1/products/reviews/', views.products_reviews_rating_api_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
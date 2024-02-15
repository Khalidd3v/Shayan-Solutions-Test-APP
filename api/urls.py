from django.urls import path
from .views import ProductAPI

urlpatterns = [
    path("products/", ProductAPI.as_view(), name="all_products"),
    path('products/<int:pk>/', ProductAPI.as_view(), name='single_product'),
]

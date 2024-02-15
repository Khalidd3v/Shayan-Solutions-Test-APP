from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer

class ProductAPI(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                product = Product.objects.get(id=pk)
                serializer = ProductSerializer(product)
                return Response({"message": "Product found", "product": serializer.data}, status=status.HTTP_200_OK)
            except Product.DoesNotExist:
                return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response({"message": "Products", "products": serializer.data}, status=status.HTTP_200_OK)

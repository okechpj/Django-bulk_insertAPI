from django.shortcuts import render
from core.models import Product, Product_variant
from .serializers import ProductSerializer, ProductVariantSerializer
from rest_framework import viewsets
from rest_framework.views import Response
from rest_framework import status

# viewset to handle create and read requests for product
class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all() # get all products
    serializer_class = ProductSerializer # specifies serializer class to use for serializing/ decerializing products instance
    
    # create request method 
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#viewset to handle create and read requests for product variants
class ProductVariantViewset(viewsets.ModelViewSet):
    queryset = Product_variant.objects.all()  # get all product_variants
    serializer_class = ProductVariantSerializer  #specifies serializer to use
    
    # create request method
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

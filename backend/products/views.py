from rest_framework import viewsets, generics
from .models import Product, Category
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .serializers import ProductSerializer, CategorySerializer, UserSerialzer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .throttling import ProductsRateThrottle, CategoryRateThrottle, SearchRateThrottle

# Create your views here.
class ProductsByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer
    throttle_classes  = [ProductsRateThrottle]

    def get_queryset(self):
        category = self.kwargs['category']

        return Product.objects.filter(category__name=category)[:10]
    
class ProductsByName(generics.ListAPIView):
    serializer_class = ProductSerializer
    throttle_classes  = [SearchRateThrottle]

    def get_queryset(self):
        name = self.kwargs['name']
 
        return Product.objects.filter(name__icontains=name) 

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    throttle_classes  = [ProductsRateThrottle]
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser, FormParser]

    def retrieve(self, request,*args, **kwargs):
        print(request.data)
        return super().retrieve(request,*args, **kwargs )

    def create(self, request, *args, **kwargs):
        print(request.data)
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        print(request.data)
        return super().update(request, *args, **kwargs)

class CategoryViewSet(viewsets.ModelViewSet):
    throttle_classes  = [CategoryRateThrottle]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
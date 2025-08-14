from rest_framework import viewsets, generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.
class ProductsByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Product.objects.filter(category__name=category)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

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
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
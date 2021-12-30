from accounts.api.permissions import IsAdminUser
from product.models import Brand, Category, GenericName, Product
from product.api.serializers import (
    AttachmentSerializer,
    BrandSerializer, 
    BrandChoicesSerializer, 
    CategorySerializer, 
    GenericNameChoicesSerializer, 
    GenericNameSerializer, 
    ProductChoicesSerializer, 
    ProductSerializer,
    ProductDetailSerializer,
)

from rest_framework import generics


## views for Category
class CategoryCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer


class CategoryListAPIView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
## views for category ends 


## views for generics starts
class GenericNameCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = GenericNameSerializer


class GenericListAPIView(generics.ListAPIView):
    serializer_class = GenericNameSerializer
    queryset = GenericName.objects.all()


class GenericUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = GenericNameSerializer
    queryset = GenericName.objects.all()


class GenericDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = GenericNameSerializer
    queryset = GenericName.objects.all()
## generic views ends here


## views for brand 
class BrandCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BrandSerializer


class BrandListAPIView(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class BrandUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class BrandDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()
## views for brand ends here


## views for product
class ProductCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    

class ProductUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

## views for product ends here

## for choices
class GetGenericNameAPIView(generics.ListAPIView):
    serializer_class = GenericNameChoicesSerializer

    def get_queryset(self):
        category = self.request.GET.get('category',None)
        queryset = GenericName.objects.all()
        return queryset.filter(category__id=category)


class GetBrandAPIView(generics.ListAPIView):
    serializer_class = BrandChoicesSerializer

    def get_queryset(self):
        # category = self.request.GET.get('category',None)
        generic = self.request.GET.get('generic',None)
        queryset = Brand.objects.all()
        return queryset.filter(generic__id=generic)


class GetProductAPIView(generics.ListAPIView):
    serializer_class = ProductChoicesSerializer

    def get_queryset(self):
        brand = self.request.GET.get('brand',None)
        queryset = Product.objects.all()
        return queryset.filter(brand__id=brand)
        

class GetProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()

## choices end

## attachment

class AttachmentCreateView(generics.CreateAPIView):
    permission_class = ['IsAllUser']
    serialier_class = AttachmentSerializer

## attachment ends
from rest_framework import serializers

from product.models import (
    Attachment, 
    Brand,
    Category, 
    Product, 
    GenericName,
)


## for creation from admin panel
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class GenericNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenericName
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

## admin panel creation ends

## for choices
class GenericNameChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenericName
        fields = ('name',)

class BrandChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('name',)

class ProductChoicesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
            max_length=None, use_url=True
        )
    class Meta:
        model = Product
        fields = ('name','price','no_of_pieces','image',)

## choices end


## for detail of product ##
class ProductDetailSerializer(serializers.ModelSerializer):
    category= CategorySerializer()
    generic= CategorySerializer()
    brand= CategorySerializer()
    image = serializers.ImageField(
            max_length=None, use_url=True
        )

    class Meta:
        model = Product
        fields = (
            'name',
            'category',
            'generic',
            'brand',
            'image',
            'description',
            'price',
            'no_of_pieces',
            'manuf_date',
            'expiry_date',
        )

## attachment serializer starts
class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ('file_name','attachment',)
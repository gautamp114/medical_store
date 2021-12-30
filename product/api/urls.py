from django.conf.urls import url
from django.urls import path

from product.api.views import (
    CategoryCreateAPIView,
    CategoryListAPIView,
    CategoryUpdateAPIView,
    CategoryDeleteAPIView,

    GenericNameCreateAPIView,
    GenericListAPIView,
    GenericUpdateAPIView,
    GenericDeleteAPIView,

    BrandCreateAPIView,
    BrandListAPIView,
    BrandUpdateAPIView,
    BrandDeleteAPIView,
    GetBrandAPIView,
    GetGenericNameAPIView,
    GetProductAPIView,

    ProductCreateAPIView,
    ProductListAPIView,
    GetProductDetailAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView,
)

## category
urlpatterns = [
    path('category-create/',CategoryCreateAPIView.as_view(), name='category_create'),
    path('category-list/',CategoryListAPIView.as_view(), name='category_list'),
    path('category-update/<int:pk>/',CategoryUpdateAPIView.as_view(), name='category_update'),
    path('category-delete/<int:pk>/',CategoryDeleteAPIView.as_view(), name='category_delete'),
]

## generic
urlpatterns = urlpatterns + [
    path('generic-create/',GenericNameCreateAPIView.as_view(), name='generic_create'),
    path('generic-list/',GenericListAPIView.as_view(), name='generic_list'),
    path('generic-update/<int:pk>/',GenericUpdateAPIView.as_view(), name='generic_update'),
    path('generic-delete/<int:pk>/',GenericDeleteAPIView.as_view(), name='generic_delete'),
]

## brand
urlpatterns = urlpatterns + [
    path('brand-create/',BrandCreateAPIView.as_view(), name='brand_create'),
    path('brand-list/',BrandListAPIView.as_view(), name='brand_list'),
    path('brand-update/<int:pk>/',BrandUpdateAPIView.as_view(), name='brand_update'),
    path('brand-delete/<int:pk>/',BrandDeleteAPIView.as_view(), name='brand_delete'),
]

##product
urlpatterns = urlpatterns + [
    path('product-create/',ProductCreateAPIView.as_view(), name='product_create'),
    path('product-list/',ProductListAPIView.as_view(), name='product_list'),
    path('product-detail/<int:pk>/',GetProductDetailAPIView.as_view(), name='product_detail'),
    path('product-update/<int:pk>/',ProductUpdateAPIView.as_view(), name='product_update'),
    path('product-delete/<int:pk>/',ProductDeleteAPIView.as_view(), name='product_delete'),
]

## for choices
urlpatterns = urlpatterns +[
    path('get-generic_name/',GetGenericNameAPIView.as_view(),name="get_generic_name"),
    path('get-brand_name/',GetBrandAPIView.as_view(),name="get_brand_name"),
    path('get-product_name/',GetProductAPIView.as_view(),name="get_product_name"),
]
     

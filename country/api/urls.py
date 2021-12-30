from country.api.views import (
    DistrictListAPIView,
    ProvinceListAPIView,

)
from django.urls import path

app_name = "country"

urlpatterns = [
    path('province/list/',ProvinceListAPIView.as_view(), name="province_list"),
    path('district/list/',DistrictListAPIView.as_view(), name='district_list'),
]
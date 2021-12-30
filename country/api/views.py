from accounts.api.permissions import IsAdminUser
from country.api.serializers import DistrictChoicesSerializer, ProvinceChoicesSerializer
from country.models import Province, District
from rest_framework import generics

class ProvinceListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProvinceChoicesSerializer
    queryset = Province.objects.all()
    

class DistrictListAPIView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = DistrictChoicesSerializer

    
    def get_queryset(self):
        country = self.request.GET.get('country',None)
        province = self.request.GET.get('province',None)
        queryset = District.objects.all()
        return queryset.filter(country__id=country).filter(province__id=province)
from country.models import District, Province
from django_filters import rest_framework as filters


class ProvinceFilter(filters.FilterSet):
    class Meta:
        model = Province
        fields = ('country',)


    def get_queryset(self,queryset):
        queryset = super().get_queryset(queryset)
        country = self.request.GET.get('country',None)
        if country == "" or not country:
            return queryset.none()
        return queryset.filter(country__id=country)


class DistrictFilter(filters.FilterSet):
    class Meta:
        model = District
        fields = ('country','province',)

    # def get_queryset(self):
    #     country = self.request.GET.get('country',None)
    #     province = self.request.GET.get('province',None)
    #     queryset = District.objects.all()
    #     return queryset.filter(country__id=country).filter(province__id=province)

        
    # def get_queryset(self,queryset):
    #     queryset = super().get_queryset(queryset)
    #     country = self.request.GET.get('country',None)
    #     province = self.request.GET.get('province',None)
    #     if country == "" or not country and province=="" or not province:
    #         return queryset.none()
    #     return queryset.filter(country__id=country).filter(province__id=province)

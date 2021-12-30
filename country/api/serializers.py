from django.db.models import fields
from country.models import Country, District, Province
from rest_framework import serializers



## for list of user
class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id','name',)

class ProvinceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('id','name',)

    
class DistrictListSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id','name',)



## for dropdown in registration form
## country will be provided from frontend and province and district accordingly      
class CountryChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id','name',)


class ProvinceChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = ('id','name',)


class DistrictChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('id','name',)


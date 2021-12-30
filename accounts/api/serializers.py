from django.db.models import fields
from rest_framework import serializers
from accounts.models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
# from rest_framework_simplejwt.serializers import TokenObtainSerializer, RefreshToken, api_settings, update_last_login

from django.contrib.auth import get_user_model

from country.api.serializers import CountryListSerializer, DistrictListSerializer, ProvinceListSerializer
User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'},validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})


    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'sex',
            'contact_number',
            'country',
            'province',
            'district',
            'password',
            'password2',
        )

    def validate(self,attrs):
        password1 = attrs['password']
        password2 = attrs['password2']

        if password1 != password2:
            raise serializers.ValidationError({'password2':"Password doesn't match"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            sex = validated_data['sex'],
            country = validated_data['country'],
            province = validated_data['province'],
            district = validated_data['district'],
            email = validated_data['email'],
            contact_number = validated_data['contact_number'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomerUserListSerializer(serializers.ModelSerializer):
    country_object = CountryListSerializer(source='country')
    province_object = ProvinceListSerializer(source='province')
    district_object = DistrictListSerializer(source='district')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'sex',
            'contact_number',
            'country_object',
            'province_object',
            'district_object',
            'password',
            'password2',
        )

# class TokenObtainPairSerializer(TokenObtainSerializer):
#     @classmethod
#     def get_token(cls, user):
#         return RefreshToken.for_user(user)

#     def validate(self, attrs):
#         data = super().validate(attrs)

#         refresh = self.get_token(self.user)

#         data['refresh'] = str(refresh)
#         data['access'] = str(refresh.access_token)
#         if self.user.is_superuser:
#             data['user_type'] = 'Admin'
#         data['user_id'] = self.user.pk
#         data['user_username'] = self.user.username

#         if api_settings.UPDATE_LAST_LOGIN:
#             update_last_login(None, self.user)

#         return data

class CustomUserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['contact_number','password']

        extra_kwargs = {
            'password': {'write_only':True}
        }
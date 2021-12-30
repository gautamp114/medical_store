from django.contrib.auth import authenticate, login
from accounts.func import add_null_to_list
from country.api.serializers import CountryChoicesSerializer
from country.models import Country
from rest_framework import generics
from accounts.api.serializers import CustomUserSerializer, CustomUserLoginSerializer ## Tokenobtainpairserializer
from accounts.models import CustomUser
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q


## registration starts
class CustomUserCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer


class CustomUserListAPIView(generics.ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class CustomUserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class CustomUserDeleteAPIView(generics.DestroyAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

## registration ends


## to login the user
class CustomUserLoginForm(generics.CreateAPIView):
    serializer_class = CustomUserLoginSerializer

    def post(self, request, format=None):
        data = self.request.data

        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                print("success")
                return Response(status=status.HTTP_200_OK)
            else:
                print("user not active")
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            print("no user")
            return Response(status=status.HTTP_404_NOT_FOUND)

class CustomAuthenticationBackend:

    def authenticate(self, request, email_or_phone=None, password=None):
        try:
             user = CustomUser.objects.get(
                 Q(email=email_or_phone) | Q(contact_number=email_or_phone)
             )
             pwd_valid = user.check_password(password)
             if pwd_valid:            
                 return user
             return None
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None

## login ends



class GetUserChoicesAPIView(generics.ListAPIView):
    model1 = Country
    serializer_class1 = CountryChoicesSerializer

    def  get_queryset(self):
        pass
    
    def list(self,request,*args,**kwargs):
        queryset1 = self.model1.objects.all()
        serializer1 = self.serializer_class1(queryset1 ,many=True)

        data = {
            'country': add_null_to_list(serializer1.data),
        }
        return Response(data)

# class TokenObtainPairView(TokenViewBase):
#     serializer_class = TokenObtainPairSerializer
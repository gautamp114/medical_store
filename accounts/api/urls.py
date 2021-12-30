
from rest_framework_simplejwt import views as jwt_views

from django.urls import path
from accounts.api.views import (
    CustomUserCreateAPIView,
    CustomUserListAPIView,
    CustomUserUpdateAPIView,
    CustomUserDeleteAPIView,

    CustomUserLoginForm,

    GetUserChoicesAPIView,
)

urlpatterns = [
    ## token authentication url
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    ## registration
    path('create/',CustomUserCreateAPIView.as_view(), name='create'),
    path('list/',CustomUserListAPIView.as_view(), name='list'),
    path('update/<int:pk>/',CustomUserUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>/',CustomUserDeleteAPIView.as_view(), name='delete'),

    ##login user
    path('login/',CustomUserLoginForm.as_view(), name="login"),

    ## user choices
    path('choices/',GetUserChoicesAPIView.as_view(),name='choices'),
]
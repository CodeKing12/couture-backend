from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


# Make all UIDB64 and tokens to be sent in a post request
urlpatterns = [
    path('signup/', views.CreateUser.as_view(), name='create_user'),
    path('activate/<str:uidb64>/<str:token>/', views.ActivateUser.as_view(), name='activate_user'),
    path('token/obtain/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_tokens'),
    path('token/verify/', TokenVerifyView.as_view(), name='verify_tokens'),
    path('confirm_mail/', views.UserDetails.as_view(), name='user_details'),
    path('verify/<str:uidb64>/<str:token>/', views.UserDetails.as_view(), name='user_details'),
    # The UIDB64, token and details to change are sent in a post request from the frontend
    path('change/', views.UserDetails.as_view(), name='user_details'),
    path('user/', views.UserDetails.as_view(), name='user_details'),
    path('user/', views.UserDetails.as_view(), name='user_details'),
]
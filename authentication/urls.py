from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('signup/', views.CreateUser.as_view(), name='create_user'),
    path('token/obtain/', TokenObtainPairView.as_view(), name='obtain_tokens'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh_tokens'),
    path('user/', views.UserDetails.as_view(), name='user_details')
]
from django.urls import path
from .views import UserSignUp, CheckAuthentiction, CurrentUserView, PasswordResetView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import include

urlpatterns = [
        path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
      path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),      
    path('signup/', UserSignUp.as_view(), name='user-signup'),
      path('reset-password/', PasswordResetView.as_view(), name='reset-password'),

    # path('login/', UserLogin.as_view(), name='user-login'),
    path('check-auth/', CheckAuthentiction.as_view(), name='check_authentication'),
    path('profile/me', CurrentUserView.as_view(), name='current_user')
]

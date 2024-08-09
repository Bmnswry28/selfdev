from django.urls import path
from .views import RegisterView,LoginView,PasswordResetView,PasswordResetConfirmView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('api/register', RegisterView.as_view(), name='register'),
    path('api/login', LoginView.as_view(), name='login'),
    path('api/password-reset', PasswordResetView.as_view(), name='password_reset'),
    path('api/password-reset-confirm/<str:token>',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
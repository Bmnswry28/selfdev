from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serilalizers import UserSerializer, LoginSerializer, PasswordResetSerializer
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import PasswordResetToken
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
import logging
logger = logging.getLogger(__name__)
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh),'access': str(refresh.access_token),}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)  
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.validated_data['username'],password=serializer.validated_data['password'])
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({'refresh': str(refresh),'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.filter(email=email).first()
                if user:
                    token = PasswordResetToken.objects.create(user=user)
                    reset_url = f'http://localhost:8000/reset-password/{token.token}'
                    send_mail(
                        'Password Reset',
                        f'Click the following link to reset your password: http://localhost:8000/api/password-reset-confirm/{token.token}',
                        settings.DEFAULT_FROM_EMAIL,
                        [email],
                        fail_silently=False,
                    )
                    return Response({"message": "Password reset email sent"}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)
            except User.DoesNotExist:
                return Response({"message": "User with this email does not exist"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetConfirmView(APIView):
    def post(self, request, token):
        logger.debug(f"Received password reset request with token: {token}")
        try:
            reset_token = PasswordResetToken.objects.get(token=token)
            if reset_token.is_valid:
                new_password = request.data.get('new_password')
                if new_password:
                    user = reset_token.user
                    user.set_password(new_password)
                    user.save()
                    reset_token.is_used = True
                    reset_token.save()
                    return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "New password is required"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)
        except PasswordResetToken.DoesNotExist:
            logger.error(f"PasswordResetToken with token {token} does not exist")
            return Response({"message": "Invalid token"}, status=status.HTTP_404_NOT_FOUND)
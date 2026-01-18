from typing import Any, TypedDict, cast

from django.contrib.auth import login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserProfileSerializer
)


class LoginData(TypedDict):
    user: Any
    access: str
    refresh: str


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "message": "User registered successfully",
                "user": UserProfileSerializer(user).data,
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = cast(LoginData, serializer.validated_data)

        user = data["user"]
        access = data["access"]
        refresh = data["refresh"]

        return Response(
            {
                "message": "Login successful",
                "tokens": {
                    "access": access,
                    "refresh": refresh,
                },
                "user": UserProfileSerializer(user).data,
            },
            status=status.HTTP_200_OK,
        )



class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(
            {"message": "Logged out successfully"},
            status=status.HTTP_200_OK,
        )

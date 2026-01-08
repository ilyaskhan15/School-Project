# accounts/views.py
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from typing import cast
from .models import User
from .serializers import UserSerializer, RegisterSerializer

class RegisterView(APIView):
    """
    User registration API endpoint
    """
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            # Create user
            user = cast(User, serializer.save())
            
            # Log the user in (optional)
            login(request, user)
            
            # Return success response with user data
            return Response({
                'message': 'Registration successful!',
                'user': UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        
        # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(generics.ListAPIView):
    """
    List all users (for testing)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
from django.shortcuts import render
from .models import Profile
from .serializers import ProfileSerializer, UserRegisterSerializer, UserListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, generics, permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


User = get_user_model()


class FollowToggleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, username):
        target_user = get_object_or_404(User, username=username)
        profile = target_user.profile

        if request.user in profile.followers.all():
            profile.followers.remove(request.user)
            return Response({"status": "unfollowed"}, status=status.HTTP_200_OK)
        else:
            profile.followers.add(request.user)
            return Response({"status": "followed"}, status=status.HTTP_201_CREATED)
        
class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'user__username'


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "status": "success",
                "data": {
                    "username": user.username,
                    "email": user.email
                }
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    

class UserListView(generics.ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAdminUser]  # 👈 Apenas admins podem listar
    
    def get_queryset(self):
        return User.objects.all().order_by('-date_joined')
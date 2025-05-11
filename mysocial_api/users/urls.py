from django.urls import path
from .views import FollowToggleView, ProfileDetailView, UserRegisterView, UserListView

urlpatterns = [
    path('api/profiles/<str:username>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('api/profiles/<str:username>/follow/', FollowToggleView.as_view(), name='follow-toggle'),
    path('api/auth/register/', UserRegisterView.as_view(), name='user-register'),
    path('api/users/', UserListView.as_view(), name='user-list'),
]

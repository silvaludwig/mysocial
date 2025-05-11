from django.urls import path
from .views import( 
    PostListCreateView, 
    PostRetrieveUpdateDestroyView, 
    CommentListCreateView, 
    CommentRetrieveUpdateDestroyView,
    )


urlpatterns = [
    path('api/posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('api/posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    path('api/posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('api/comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail'),
]

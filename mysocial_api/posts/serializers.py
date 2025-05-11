from rest_framework import serializers
from .models import Post, Comment, Reaction
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ReactionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Reaction
        fields = ['user', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    like_count = serializers.SerializerMethodField()
    dislike_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'content', 'like_count', 'dislike_count', 'created_at']
    
    def get_like_count(self, obj):
        return obj.reactions.filter(reaction_type=Reaction.LIKE).count()
    
    def get_dislike_count(self, obj):
        return obj.reactions.filter(reaction_type=Reaction.DISLIKE).count()


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'




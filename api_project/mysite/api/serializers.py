from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import BlogPost

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Add user groups
        token['groups'] = list(user.groups.values_list('name', flat=True))
        
        # Add user permissions
        token['permissions'] = list(user.user_permissions.values_list('codename', flat=True))
        
        # Optionally add all permissions (including group permissions)
        token['all_permissions'] = list(user.get_all_permissions())
        
        # You can also add other user info
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser
        
        return token

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'published_date']
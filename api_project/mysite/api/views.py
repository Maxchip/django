from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from .models import BlogPost
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import BlogPostSerializer, CustomTokenObtainPairSerializer

# Create your views here.

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Check permission for GET (list)"""
        user = self.request.user
        
        # Check if user has specific permission
        if not user.has_perm('api.view_blogpost'):
            raise PermissionDenied("You don't have permission to view blog posts")
        
        return BlogPost.objects.all()

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]
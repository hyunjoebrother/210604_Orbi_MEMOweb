from django.shortcuts import render

from rest_framework import viewsets
from .serializers import BlogSerializer
from .models import Blog

# Create your views here.

# API 제공해주는 view
class BlogView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

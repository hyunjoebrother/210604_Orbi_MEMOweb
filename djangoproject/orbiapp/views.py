from django.shortcuts import render

from rest_framework import viewsets
from .serializers import BlogSerializer
from .models import Blog

from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings
import os

# Create your views here.

# API 제공해주는 view
class BlogView(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

# Front에서 만든 경로들 보내주기
class ReactAppView(View):

    def get(self, request):
        try:
            with open(os.path.join(str(settings.ROOT_DIR),
                                    'djangoproject',
                                    'build',
                                    'main.html')) as file:
                return HttpResponse(file.read())

        except:
            return HttpResponse(status=501,)
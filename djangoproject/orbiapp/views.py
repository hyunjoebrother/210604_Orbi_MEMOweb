from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

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


# Django CRUD

def main(request) :
    return render(request, 'main.html')

def home(request) :
    blog_objects = Blog.objects.all()
    return render(request, 'home.html', {'blog' : blog_objects})

def post_read(request, id) :
    blog_object = get_object_or_404(Blog, pk = id)
    return render(request, 'post_read.html', {'blog' : blog_object})


def post_create(request) :
    if request.method == 'POST' :
        blog_object = Blog()
        blog_object.title = request.POST['title']
        blog_object.created_date = timezone.datetime.now()
        blog_object.body = request.POST['body']
        blog_object.save()   

        return redirect('/orbimemo/' + str(blog_object.id))
    
    return render(request, 'post_create.html')


def post_edit(request, id) :
    blog_object = get_object_or_404(Blog, pk = id)

    if request.method == 'POST' :
        blog_object.title = request.POST['title']
        blog_object.body = request.POST['body']
        blog_object.save()   

        return redirect('/orbimemo/' + str(blog_object.id))
    
    return render(request, 'post_edit.html', {'blog' : blog_object})


def post_delete(request, id) :
    blog_object = get_object_or_404(Blog, pk = id)
    blog_object.delete()

    return redirect('/')
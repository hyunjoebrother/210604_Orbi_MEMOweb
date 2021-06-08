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
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs' : blogs})

def post_read(request, blog_id) :
    blog_object = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'post_read.html', {'blog' : blog_object})

def post_create(request) :
    create_blog = Blog()

    create_blog.title = request.GET['title']
    create_blog.created_date = timezone.datetime.now()
    create_blog.body = request.GET['body']

    create_blog.save()

    return redirect('/orbimemo/' + str(create_blog.id))


def post_edit(request, edit_id) :
    blog_edit = Blog.objects.get(id = edit_id)
    return render(request, 'post_edit.html', {'blog' : blog_edit})

def post_update(request, update_id) :
    update_blog = Blog.objects.get(id = update_id)

    update_blog.title = request.GET['title']
    update_blog.created_date = timezone.datetime.now()
    update_blog.body = request.GET['body']

    update_blog.save()

    return redirect('/orbimemo/' + str(update_blog.id))


def post_delete(request, delete_id) :
    delete_blog = Blog.objects.get(id = delete_id)
    delete_blog.delete()

    return redirect('/')
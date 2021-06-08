"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import View
from rest_framework import routers
import orbiapp.views

router = routers.DefaultRouter()
router.register('blog', orbiapp.views.BlogView, 'blog')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('react/', orbiapp.views.ReactAppView.as_view()),

    path('', orbiapp.views.main, name = 'main'),
    path('home/', orbiapp.views.home, name = 'home'),
    path('orbimemo/<int:blog_id>', orbiapp.views.post_read, name = 'detail'),

    path('orbimemo/create', orbiapp.views.post_create, name = 'create'),
    path('orbimemo/edit/<int:blog_id>', orbiapp.views.post_edit, name = 'edit'),
    path('orbimemo/update/<int:blog_id>', orbiapp.views.post_update, name = 'update'),
    path('orbimemo/delete/<int:blog_id>', orbiapp.views.post_delete, name = 'delete'),
]

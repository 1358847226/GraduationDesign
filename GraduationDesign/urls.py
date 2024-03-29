"""GraduationDesign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.template.defaulttags import url
from django.urls import path
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token

from GraduationDesign import views

urlpatterns = [
    # 用户部分
    path('admin/', admin.site.urls),
    path('api/login', obtain_jwt_token),
    # 页面部分
    path('', TemplateView.as_view(template_name='index.html')),
    path('Product', TemplateView.as_view(template_name='product/index.html')),
    # 接口部分
    path('api/health', views.health),
    path('api/Products/', views.ProductList.as_view()),
    path('api/Product/<int:pk>/', views.ProductDetail.as_view()),
]

#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@File       :views.py
@Function   :
@Time       :2023/3/7 9:39
@Author     :NothingToStay
@Softwate   :PyCharm
@License    :copyright ©2011-2023 Valve Dota2
"""
from django.contrib import auth
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_protect
from rest_framework import mixins, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from GraduationDesign import models, Serializers


def health(request):
    """
    健康检查接口
    :param request:
    :return:
    """
    return JsonResponse({'code': 200, 'message': '成功'})


class ProductList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = models.Product.objects.all()
    serializer_class = Serializers.ProductSerializer
    authentication_classes = [JSONWebTokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def post(self, req, *arg, **kw):
        return self.create(req, *arg, *kw)

    def get(self, req, *arg, **kw):
        return self.list(req, *arg, **kw)


class ProductDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = models.Product.objects.all()
    serializer_class = Serializers.ProductSerializer

    def get(self, req, *arg, **kw):
        return self.retrieve(req, *arg, **kw)

    def put(self, req, *arg, **kw):
        return self.update(req, *arg, **kw)

    def delete(self, req, *arg, **kw):
        return self.delete(req, *arg, **kw)


class Login(APIView):

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'status': True,
            'token': token.key,
            'user_id': user.pk,
            'user_name': user.username,
        })

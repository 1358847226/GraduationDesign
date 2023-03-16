#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@File       :Serializers.py
@Function   :
@Time       :2023/3/7 15:31
@Author     :NothingToStay
@Software   :PyCharm
@License    :copyright ©2011-2023 Valve Dota2
"""
import time

from rest_framework import serializers

from GraduationDesign import models
from GraduationDesign.models import Product


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=15, required=False, default='无标题')
    source = serializers.CharField(max_length=50, required=False, default='未知来源')
    author = serializers.CharField(max_length=20, required=False, default='佚名')
    content = serializers.CharField(max_length=5000, required=False, default='')
    main_image = serializers.CharField(max_length=255, required=False, default='')
    images = serializers.CharField(max_length=500, required=False, default='')
    show = serializers.BooleanField(required=False, default=False)
    download_num = serializers.IntegerField(required=False, default=0)
    browse_num = serializers.IntegerField(required=False, default=0)
    upload_time = serializers.TimeField(required=False, default=time.time())

    def create(self, validated_data):
        return models.Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.source = validated_data.get('source', instance.source)
        instance.author = validated_data.get('author', instance.author)
        instance.main_image = validated_data.get('main_image', instance.main_image)
        instance.images = validated_data.get('images', instance.images)
        instance.show = validated_data.get('show', instance.show)
        instance.download_num = validated_data.get('download_num', instance.download_num)
        instance.browse_num = validated_data.get('browse_num', instance.browse_num)
        instance.save()
        return instance

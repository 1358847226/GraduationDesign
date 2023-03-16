#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@File       :models.py
@Function   :
@Time       :2023/3/7 11:14
@Author     :NothingToStay
@Software   :PyCharm
@License    :copyright ©2011-2023 Valve Dota2
"""
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=15, verbose_name='项目名')
    source = models.CharField(max_length=50, verbose_name='项目来源')
    author = models.CharField(max_length=20, verbose_name='项目作者')
    content = models.CharField(max_length=5000, verbose_name='正文')
    main_image = models.CharField(max_length=255, verbose_name='项目主图')
    images = models.CharField(max_length=500, verbose_name='项目截图')
    show = models.BooleanField(verbose_name='是否显示')
    download_num = models.IntegerField(verbose_name='下载量')
    browse_num = models.IntegerField(verbose_name='浏览量')
    upload_time = models.DateField(verbose_name='上传时间', auto_now_add=True)

    def __str__(self):
        return f'<Product {self.title}>'

    class Meta:
        db_table = 'product'
        app_label = 'GraduationDesign'
        ordering = ['upload_time']

from django.contrib import admin
from django.test import TestCase

# Create your tests here.
from GraduationDesign import models

admin.site.register(models.Product)

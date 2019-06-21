# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 15:07:24 2019

@author: dnsusr04
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
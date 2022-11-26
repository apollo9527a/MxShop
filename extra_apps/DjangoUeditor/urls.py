# -*- coding: utf-8 -*-
import django
from .views import get_ueditor_controller

DJANGO_VERSION = django.VERSION[:2]


if DJANGO_VERSION >= (1, 8):
    from django.urls import re_path
    urlpatterns = [
        re_path(r'^controller/$', get_ueditor_controller)
    ]

else:
    try:
        from django.conf.urls import patterns, url
    except ImportError:
        from django.urls import patterns, re_path

    urlpatterns = patterns('',
        re_path(r'^controller/$', get_ueditor_controller)
    )

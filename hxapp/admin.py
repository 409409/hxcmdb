# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(Idc)
admin.site.register(Host)
admin.site.register(User)
admin.site.register(Order)
# Register your models here.

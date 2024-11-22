from django.contrib import admin

# Register your models here.

from .models import Vehicle #用于存储停车场中车辆的基本信息和状态。

admin.site.register(Vehicle)

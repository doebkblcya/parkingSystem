from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # 在列表页显示的字段
    list_display = ('username', 'user_type', 'is_staff', 'is_active', 'date_joined')
    
    # 添加可以筛选的字段
    list_filter = ('user_type', 'is_staff', 'is_active')
    
    # 添加搜索字段
    search_fields = ('username',)
    
    # 在编辑页面添加 user_type 字段
    fieldsets = UserAdmin.fieldsets + (
        ('用户类型', {'fields': ('user_type',)}),
    )
    
    # 在创建用户页面添加 user_type 字段
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('用户类型', {'fields': ('user_type',)}),
    )

# 注册模型
admin.site.register(CustomUser, CustomUserAdmin)

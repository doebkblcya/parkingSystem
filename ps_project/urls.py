"""
URL configuration for ps_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import redirect

# 判断用户是否已登录，跳转到相应的页面
def home_redirect(request):
    if request.user.is_authenticated:
        # 已登录用户跳转到停车管理首页
        return redirect('parking:index')
    else:
        # 未登录用户跳转到登录页面
        return redirect('user:login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),  # 用户认证相关功能
    path('parking/', include('parking.urls')),  # 停车管理功能
    path('', home_redirect),  # 根路径判断是否登录并重定向
]


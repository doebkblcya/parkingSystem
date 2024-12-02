from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # 导入视图文件中的函数

app_name = 'user'  # 设置 app_name，确保模板中的 URL 标签可以正确解析

urlpatterns = [
    # 登录视图
    path('login/', views.login_view, name='login'),

    # 注销视图
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # 注册视图
    path('register/', views.register, name='register'),

    # 车主登录视图
    path('owner/login/', views.owner_login_view, name='owner_login'),
]

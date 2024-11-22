from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # 用户注册
    path('login/', views.login_view, name='login'),  # 用户登录
    path('logout/', views.logout_view, name='logout'),  # 用户登出
]
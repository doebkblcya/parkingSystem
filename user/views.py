from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# 用户注册视图
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # 保存新用户
            login(request, user)  # 用户注册成功后直接登录
            return redirect('parking:index')  # 注册后跳转到停车场首页
    else:
        form = UserCreationForm()  # 显示空的注册表单
    return render(request, 'user/register.html', {'form': form})  # 返回注册页面并传递表单

# 用户登录视图
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # 使用Django的内置认证表单
        if form.is_valid():
            user = form.get_user()  # 获取表单中的用户
            login(request, user)  # 登录用户
            return redirect('parking:index')  # 登录成功后跳转到停车场首页
    else:
        form = AuthenticationForm()  # 显示空的登录表单
    return render(request, 'user/login.html', {'form': form})  # 返回登录页面并传递表单

# 用户注销视图
def logout_view(request):
    logout(request)  # 注销当前用户
    return redirect('user:login')  # 注销后跳转到登录页面

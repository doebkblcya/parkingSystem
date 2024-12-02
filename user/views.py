from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomLoginForm, CustomUserCreationForm
from django.contrib import messages

# 统一的注册视图
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.user_type == 'owner':
                return redirect('parking:owner_dashboard')
            return redirect('parking:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})

# 管理员登录视图
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser or user.user_type == 'admin':
                    login(request, user)
                    return redirect('parking:index')
                else:
                    messages.error(request, '该账号不是管理员账号')
            else:
                messages.error(request, '用户名或密码错误')
    else:
        form = CustomLoginForm()
    return render(request, 'user/login.html', {'form': form})

# 用户注销视图
def logout_view(request):
    logout(request)
    return redirect('user:login')

# 车主登录视图
def owner_login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.user_type == 'owner':
                    login(request, user)
                    return redirect('parking:owner_dashboard')
                else:
                    messages.error(request, '该账号不是车主账号')
            else:
                messages.error(request, '用户名或密码错误')
    else:
        form = CustomLoginForm()
    return render(request, 'user/owner_login.html', {'form': form})

# 车主注册视图
def owner_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'owner'  # 强制设置为车主类型
            user.save()
            login(request, user)
            return redirect('parking:owner_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/owner_register.html', {'form': form})

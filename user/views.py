from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 用户注册成功后直接登录
            return redirect('index')  # 跳转到主页
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # 登录成功后跳转到主页
    else:
        form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form})

def logout_view(request):
    logout(request)  # 登出用户
    return redirect('index')  # 登出后跳转到主页
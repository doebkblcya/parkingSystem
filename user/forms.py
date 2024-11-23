from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    # 定义登录表单字段，并添加Bootstrap样式
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"})  # 添加 Bootstrap 样式
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={"class": "form-control"})  # 添加 Bootstrap 样式
    )

class UserRegistrationForm(forms.Form):
    # 定义注册表单字段，并添加Bootstrap样式
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"})  # 添加 Bootstrap 样式
    )
    password1 = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={"class": "form-control"})  # 添加 Bootstrap 样式
    )
    password2 = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(attrs={"class": "form-control"})  # 添加 Bootstrap 样式
    )

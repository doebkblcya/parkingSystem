from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', '管理员'),
        ('owner', '车主'),
    )
    
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default='admin',
        verbose_name='用户类型'
    )
    
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

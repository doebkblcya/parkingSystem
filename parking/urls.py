from django.urls import path
from . import views

app_name = 'parking'

urlpatterns = [
    path('', views.index, name='index'),  # 停车管理主页
    path('entry/', views.vehicle_entry, name='vehicle_entry'),  # 车辆入场登记
    path('exit/<str:license_plate>/', views.vehicle_exit, name='vehicle_exit'),  # 车辆出场登记
    path('list/', views.vehicle_list, name='vehicle_list'),  # 车辆当前状态列表
    path('history/', views.vehicle_history, name='vehicle_history'),  # 车辆历史记录
]

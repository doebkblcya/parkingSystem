from django.urls import path
from . import views

# app_name = 'parking'

# 1. vehicle_entry
# URL路径：/entry/
# 功能：用于车辆进场登记，显示登记表单并处理用户提交的数据。
# 使用场景：当停车场管理员需要添加新车辆时。
# 2. vehicle_exit
# URL路径：/exit/<str:license_plate>/
# 功能：根据车牌号标记车辆出场，更新车辆状态和离开时间。
# 使用场景：管理员为车辆登记离开时。
# 注意：<str:license_plate> 是动态路径参数，用于传递车牌号。
# 3. vehicle_list
# URL路径：/list/
# 功能：显示所有当前在场的车辆列表。
# 使用场景：管理员查看停车场当前状况。
# 4. vehicle_history
# URL路径：/history/
# 功能：查询所有已出场车辆的历史记录。
# 使用场景：管理员查询车辆的进出记录。

urlpatterns = [
    # 主页视图
    path('', views.index, name='index'),
    
    # 车辆进场登记
    path('entry/', views.vehicle_entry, name='vehicle_entry'),
    
    # 车辆出场登记
    path('exit/<str:license_plate>/', views.vehicle_exit, name='vehicle_exit'),
    
    # 当前车辆列表
    path('list/', views.vehicle_list, name='vehicle_list'),
    
    # 历史记录查询
    path('history/', views.vehicle_history, name='vehicle_history'),
]
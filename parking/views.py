from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from .models import Vehicle
from .forms import VehicleForm

# Create your views here.

# 基本功能：
# vehicle_entry：车辆进场登记。
# vehicle_exit：车辆出场登记。
# vehicle_list：当前车辆列表。
# vehicle_history：历史记录查询。
# 扩展功能：
# vehicle_detail：车辆详情。
# parking_statistics：停车场统计。

# index: 主页。

def index(request):
    vehicles = Vehicle.objects.filter(status='in')  # 获取所有在场的车辆
    current_vehicle_count = Vehicle.objects.filter(status='in').count()
    return render(request, 'parking/index.html', {'vehicles': vehicles,'current_vehicle_count': current_vehicle_count,})

def vehicle_entry(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()  # 保存到数据库
            return redirect('vehicle_list')  # 跳转到车辆列表
    else:
        form = VehicleForm()
    return render(request, 'parking/vehicle_entry.html', {'form': form})

def vehicle_exit(request, license_plate):
    vehicle = get_object_or_404(Vehicle, license_plate=license_plate, status='in')
    vehicle.exit_time = now()
    vehicle.status = 'out'
    vehicle.save()
    return redirect('vehicle_list')  # 跳转到车辆列表

def vehicle_list(request):
    vehicles = Vehicle.objects.filter(status='in')  # 当前在场车辆
    return render(request, 'parking/vehicle_list.html', {'vehicles': vehicles})

def vehicle_history(request):
    vehicles = Vehicle.objects.filter(status='out')  # 已出场车辆
    return render(request, 'parking/vehicle_history.html', {'vehicles': vehicles})
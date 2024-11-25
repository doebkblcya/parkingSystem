from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Vehicle
from .forms import VehicleForm

# Create your views here.

@login_required
def index(request):
    vehicles = Vehicle.objects.filter(status='in')  # 获取所有在场的车辆
    current_vehicle_count = vehicles.count()  # 计算当前在场车辆数量
    return render(request, 'parking/index.html', {'vehicles': vehicles, 'current_vehicle_count': current_vehicle_count})

@login_required
def vehicle_entry(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()  # 保存到数据库
            return redirect('parking:vehicle_list')  # 跳转到车辆列表（使用app_name）
    else:
        form = VehicleForm()
    return render(request, 'parking/vehicle_entry.html', {'form': form})

@login_required
def vehicle_exit(request, license_plate):
    # 查找车辆并确保其状态是 'in'（在场）
    vehicle = get_object_or_404(Vehicle, license_plate=license_plate, status='in')
    vehicle.exit_time = now()  # 记录出场时间
    vehicle.status = 'out'  # 修改车辆状态为 'out'
    vehicle.save()  # 保存更改
    return redirect('parking:vehicle_list')  # 跳转到车辆列表（使用app_name）

@login_required
def vehicle_list(request):
    # 获取所有状态为 "in" 的车辆（假设在场状态为 'in'）
    vehicles = Vehicle.objects.filter(status='in')
    return render(request, 'parking/vehicle_list.html', {'vehicles': vehicles})

@login_required
def vehicle_history(request):
    # 获取已出场的车辆
    vehicles = Vehicle.objects.filter(status='out')
    return render(request, 'parking/vehicle_history.html', {'vehicles': vehicles})

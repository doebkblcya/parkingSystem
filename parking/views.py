from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from datetime import datetime
from .models import Vehicle, ParkingSettings
from .forms import VehicleForm, ParkingSettingsForm

# Create your views here.

@login_required
def index(request):
    total_vehicles = Vehicle.objects.count()
    large_vehicles = Vehicle.objects.filter(vehicle_type='large').count()
    small_vehicles = Vehicle.objects.filter(vehicle_type='small').count()

    # 其他需要在首页显示的内容
    recent_entries = Vehicle.objects.order_by('-entry_time')[:5]

    context = {
        'total_vehicles': total_vehicles,
        'large_vehicles': large_vehicles,
        'small_vehicles': small_vehicles,
        'recent_entries': recent_entries,
    }
    return render(request, 'parking/index.html', context)

@login_required
def vehicle_entry(request):
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            settings = ParkingSettings.objects.first()
            total_spots = settings.total_spots

            # 判断车位是否已满
            current_vehicles = Vehicle.objects.filter(exit_time__isnull=True).count()
            if current_vehicles >= total_spots:
                messages.error(request, "停车场已满，无法入场！")
                return redirect('parking:index')

            vehicle = form.save(commit=False)
            vehicle.entry_time = now()
            vehicle.save()

            return redirect('parking:vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'parking/vehicle_entry.html', {'form': form})


@login_required
def vehicle_exit(request, license_plate):
    # 查找车辆并确保其状态是 'in'（在场）
    vehicle = get_object_or_404(Vehicle, license_plate=license_plate, status='in',exit_time__isnull=True)
    exit_time = datetime.now()
    vehicle.exit_time = now()  # 记录出场时间
    vehicle.status = 'out'  # 修改车辆状态为 'out'
    
    parked_hours = (exit_time - vehicle.entry_time).total_seconds() / 3600
    hourly_rate = settings.PARKING_HOURLY_RATE
    vehicle.payment_amount = round(parked_hours * hourly_rate, 2)
    
    vehicle.save()  # 保存更改
    
    messages.success(request, f"车辆 {vehicle.license_plate} 已离场，应缴费用：{vehicle.payment_amount} 元")
    return redirect('parking:vehicle_list')  # 跳转到车辆列表

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

@login_required
def settings_view(request):
    # 获取或创建唯一的一条系统设置记录
    settings_instance, _ = ParkingSettings.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = ParkingSettingsForm(request.POST, instance=settings_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "设置已更新")
            return redirect('parking:index')
    else:
        form = ParkingSettingsForm(instance=settings_instance)
    return render(request, 'parking/settings.html', {'form': form})

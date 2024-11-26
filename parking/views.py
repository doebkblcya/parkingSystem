from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from datetime import timedelta
from .models import Vehicle, ParkingSettings
from .forms import VehicleForm, ParkingSettingsForm
from decimal import Decimal
from django.db.models import Sum

@login_required
def index(request):
    """主页视图，展示车辆统计和最近记录"""
    
    # 统计状态为 'in' 的车辆总数和各类型车辆数量
    in_vehicles = Vehicle.objects.filter(status='in')
    total_in_vehicles = in_vehicles.count()
    large_in_vehicles = in_vehicles.filter(vehicle_type='large').count()
    small_in_vehicles = in_vehicles.filter(vehicle_type='small').count()

    # 统计状态为 'out' 的车辆总数和各类型车辆数量
    out_vehicles = Vehicle.objects.filter(status='out')
    total_out_vehicles = out_vehicles.count()
    large_out_vehicles = out_vehicles.filter(vehicle_type='large').count()
    small_out_vehicles = out_vehicles.filter(vehicle_type='small').count()

    # 统计状态为 'out' 的车辆的缴费金额总计
    total_payment_out = out_vehicles.aggregate(total_payment=Sum('payment_amount'))['total_payment'] or 0

    # 获取最近入场的 5 条记录
    recent_entries = in_vehicles.order_by('-entry_time')[:5]

    # 渲染到模板
    context = {
        'total_in_vehicles': total_in_vehicles,
        'large_in_vehicles': large_in_vehicles,
        'small_in_vehicles': small_in_vehicles,
        'total_out_vehicles': total_out_vehicles,
        'large_out_vehicles': large_out_vehicles,
        'small_out_vehicles': small_out_vehicles,
        'total_payment_out': total_payment_out,
        'recent_entries': recent_entries,
    }
    
    return render(request, 'parking/index.html', context)


@login_required
def vehicle_entry(request):
    """车辆入场视图"""
    if request.method == "POST":
        form = VehicleForm(request.POST)
        if form.is_valid():
            # 获取车辆的车牌号
            license_plate = form.cleaned_data['license_plate']

            # 检查是否已存在在场的车辆
            existing_vehicle = Vehicle.objects.filter(license_plate=license_plate, status='in').first()

            # 如果存在状态为 'in' 的车辆，提示重复
            if existing_vehicle:
                form.add_error('license_plate', '该车牌号已在场，不能重复入场！')
                return render(request, 'parking/vehicle_entry.html', {'form': form})

            # 获取系统设置中的车位数
            settings_instance = ParkingSettings.objects.first()
            total_spots = settings_instance.total_spots if settings_instance else 100

            # 判断当前停车场是否已满
            current_vehicles = Vehicle.objects.filter(exit_time__isnull=True).count()
            if current_vehicles >= total_spots:
                messages.error(request, "停车场已满，无法入场！")
                return redirect('parking:index')

            # 如果车牌号已经离场（状态为 'out'），则新增一条记录
            # 查找该车牌号的车辆并判断其状态
            vehicle = Vehicle.objects.filter(license_plate=license_plate, status='out').first()

            if vehicle:
                # 创建一条新的车辆记录
                new_vehicle = Vehicle(
                    license_plate=vehicle.license_plate,
                    vehicle_type=vehicle.vehicle_type,  # 保留原来的车辆类型
                    entry_time=now(),  # 设置新入场时间
                    status='in'  # 新记录的状态为 'in'
                )
                new_vehicle.save()
            else:
                # 如果没有车辆记录，则创建一辆新车
                vehicle = form.save(commit=False)
                vehicle.entry_time = now()
                vehicle.status = 'in'
                vehicle.save()

            messages.success(request, f"车辆 {license_plate} 已成功入场！")
            return redirect('parking:vehicle_list')
    else:
        form = VehicleForm()

    return render(request, 'parking/vehicle_entry.html', {'form': form})


@login_required
def vehicle_exit(request, license_plate):
    """车辆离场视图"""
    # 查找在场的车辆
    vehicle = get_object_or_404(Vehicle, license_plate=license_plate, status='in', exit_time__isnull=True)
    exit_time = now()
    vehicle.exit_time = exit_time  # 设置离场时间
    vehicle.status = 'out'  # 修改状态为 'out'

    # 计算停车时长（小时），并根据系统设置计算费用
    parked_seconds = (exit_time - vehicle.entry_time).total_seconds()
    parked_hours = Decimal(parked_seconds) / Decimal(3600)  # 确保使用 Decimal 类型

    settings_instance = ParkingSettings.objects.first()
    hourly_rate = Decimal(settings_instance.hourly_rate) if settings_instance else Decimal('10.00')  # 默认收费 10 元/小时

    vehicle.payment_amount = (parked_hours * hourly_rate).quantize(Decimal('0.01'))  # 保留两位小数

    # 保存更新信息
    vehicle.save()
    messages.success(request, f"车辆 {vehicle.license_plate} 已离场，应缴费用：{vehicle.payment_amount} 元")
    return redirect('parking:vehicle_list')

@login_required
def vehicle_list(request):
    """在场车辆列表视图"""
    vehicles = Vehicle.objects.filter(status='in')
    return render(request, 'parking/vehicle_list.html', {'vehicles': vehicles})

@login_required
def vehicle_history(request):
    """车辆出场记录视图"""
    vehicles = Vehicle.objects.filter(status='out')
    return render(request, 'parking/vehicle_history.html', {'vehicles': vehicles})

@login_required
def settings_view(request):
    """系统设置视图"""
    # 获取或创建唯一的一条系统设置记录
    settings_instance, created = ParkingSettings.objects.get_or_create(
        id=1, defaults={'total_spots': 100, 'hourly_rate': 10}
    )
    if request.method == 'POST':
        form = ParkingSettingsForm(request.POST, instance=settings_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "设置已更新")
            return redirect('parking:index')
    else:
        form = ParkingSettingsForm(instance=settings_instance)
    return render(request, 'parking/settings.html', {'form': form})

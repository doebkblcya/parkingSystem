from django.db import models

# Create your models here.

# license_plate：车牌号（字符串，唯一）。
# vehicle_type：车辆类型（如小型车、大型车，选择字段）。
# entry_time：进入停车场的时间（日期时间）。
# exit_time：离开停车场的时间（日期时间，可为空）。
# status：当前状态（选择字段，例如 "在场" 或 "已离开"）。
class Vehicle(models.Model):
    license_plate = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(
        max_length=20,
        choices=[
            ('small', '小型车'),
            ('large', '大型车'),
        ],
        default='small'
    )
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=[
            ('in', '在场'),
            ('out', '已离开'),
        ],
        default='in'
    )
    # 缴费金额
    payment_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="缴费金额")

    def __str__(self):
        return self.license_plate

class ParkingSettings(models.Model):
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, default=10.00, verbose_name="每小时停车费")
    total_spots = models.PositiveIntegerField(default=100, verbose_name="总车位数")

    def __str__(self):
        return f"设置 - 每小时收费: {self.hourly_rate}元, 总车位: {self.total_spots}"

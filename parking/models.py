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

    def __str__(self):
        return self.license_plate

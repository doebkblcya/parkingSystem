from django import forms
from .models import Vehicle

# 在Django中，通常为了处理用户提交的数据（例如车辆进场登记中的车牌号和车辆类型），会创建一个 表单类（Form Class），用于验证和处理用户输入。这是Django提供的一种标准方式，能确保用户输入的数据符合要求并简化数据保存操作。

# 为什么需要表单类？
# 验证用户输入：
# 确保用户提交的数据符合特定规则（例如车牌号格式不能有特殊字符）。
# 简化数据处理：
# 自动将表单数据映射到模型字段并保存到数据库。
# 生成HTML表单：
# Django的表单类可以自动生成HTML表单，并渲染到前端页面中。

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle  # 关联的模型
        fields = ['license_plate', 'vehicle_type']  # 需要在表单中包含的字段
        widgets = {
            'license_plate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入车牌号'}),
            'vehicle_type': forms.Select(attrs={'class': 'form-control', 'placeholder': '请选择车辆类型'}),
        }
        # 自定义标签
        labels = {
            'license_plate': '车牌号',  
            'vehicle_type': '车辆类型',
        }
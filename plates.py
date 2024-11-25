import random
import string

# 定义中国省份的首字母
provinces = [
    "京", "津", "沪", "渝", "冀", "晋", "蒙", "辽", "吉", "黑", "沪", "苏", "浙", "皖", "闽",
    "赣", "鲁", "豫", "鄂", "湘", "粤", "琼", "川", "贵", "云", "陕", "甘", "青", "宁", "新"
]

# 生成随机车牌号的函数
def generate_license_plate():
    province = random.choice(provinces)  # 随机选择一个省份
    city_letter = random.choice(string.ascii_uppercase)  # 随机选择一个字母代表城市
    
    # 确保后五位最多包含两个字母
    num_letters = random.randint(0, 2)  # 随机决定字母的数量（0, 1, 或 2）
    
    # 生成字母部分
    letters = ''.join(random.choices(string.ascii_uppercase, k=num_letters))
    
    # 生成数字部分（剩余位置填充数字）
    digits = ''.join(random.choices(string.digits, k=5 - num_letters))
    
    # 将字母和数字混合并打乱顺序
    random_chars = list(letters + digits)
    random.shuffle(random_chars)
    
    # 返回完整的车牌号
    return province + city_letter + ''.join(random_chars)

# 主程序：让用户输入要生成几个车牌号
def main():
    try:
        num_plates = int(input("请输入要生成几个车牌号: "))  # 用户输入生成车牌的数量
        for _ in range(num_plates):
            print(generate_license_plate())
    except ValueError:
        print("请输入一个有效的数字")

if __name__ == "__main__":
    main()

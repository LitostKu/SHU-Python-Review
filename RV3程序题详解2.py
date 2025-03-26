import random

# 定义身份证号前 17 位数字对应的系数
coefficients = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
# 定义余数对应的校验位
check_digits = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

# 生成 100 个合法的身份证号
for _ in range(100):
    # 生成一个 17 位的整数
    id_17_digits = str(random.randint(10**16, 10**17 - 1))
    # 初始化乘积和
    total_product = 0
    # 遍历 17 位数字，计算每个数字与对应系数的乘积并求和
    for i in range(17):
        total_product += int(id_17_digits[i]) * coefficients[i]
    # 计算乘积和与 11 的模
    remainder = total_product % 11
    # 根据余数获取对应的校验位
    check_digit = check_digits[remainder]
    # 将校验位添加到 17 位数字末尾，形成 18 位身份证号
    id_18_digits = id_17_digits + check_digit
    # 输出生成的 18 位身份证号
    print(id_18_digits)
# 获取用户输入的姓名
name = input("姓名:")

# 循环确保输入的体温在 35℃ 至 42℃ 之间
while True:
    try:
        # 获取用户输入的体温
        temperature = float(input("体温:"))
        if 35 <= temperature <= 42:
            break
        else:
            print("输入的体温不在 35℃ 至 42℃ 之间，请重新输入。")
    except ValueError:
        print("输入的体温不是有效的数字，请重新输入。")

# 判断体温是否大于 37℃
if temperature > 37:
    # 若体温大于 37℃，进行重测体温
    while True:
        try:
            # 获取重测体温
            retest_temperature = float(input("重测体温:"))
            if 35 <= retest_temperature <= 42:
                break
            else:
                print("输入的重测体温不在 35℃ 至 42℃ 之间，请重新输入。")
        except ValueError:
            print("输入的重测体温不是有效的数字，请重新输入。")

    # 根据重测体温结果输出相应信息
    if retest_temperature > 37:
        print(f"{name}重测体温异常，进留观室")
    else:
        print(f"{name}重测体温正常，消毒后进教室")
else:
    # 若初始体温不大于 37℃，直接输出正常信息
    print(f"{name}体温正常，消毒后进教室")
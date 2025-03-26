# 从用户输入中读取学生人数和判断题数量，以空格分隔，并分别赋值给 stu 和 ques
stu, ques = input().split()
# 将 stu 和 ques 从字符串类型转换为整数类型
stu, ques = int(stu), int(ques)

# 从用户输入中读取每道题的满分值，以空格分隔，使用 map 函数将每个元素转换为整数，再转换为列表赋值给 sco
sco = list(map(int, input().split()))
# 从用户输入中读取每道题的正确答案，以空格分隔，使用 map 函数将每个元素转换为整数，再转换为列表赋值给 tw
tw = list(map(int, input().split()))

# 创建一个空字典 per，用于存储每道题的正确率
per = {}
# 初始化变量 t 为 0，用于统计回答正确的总人数
t = 0
# 初始化变量 sco1 为 0，用于存储每个学生的得分
sco1 = 0
# 创建一个空列表 scolst，用于存储每个学生的得分
scolst = []

# 遍历每个学生
for i in range(0, stu):
    # 从用户输入中读取当前学生的答案，以空格分隔，使用 map 函数将每个元素转换为整数，再转换为列表赋值给 ans
    ans = list(map(int, input().split()))
    j = 0
    # 初始化当前学生的得分 sco1 为 0
    sco1 = 0
    # 遍历当前学生的每一个答案
    while j < ques:
        # 判断当前学生的答案是否与正确答案相同
        if ans[j] == tw[j]:
            # 如果相同，将该题的满分值加到当前学生的得分 sco1 中
            sco1 += sco[j]
            # 回答正确的总人数 t 加 1
            t += 1
            # 计算当前题目的正确率，并以字符串形式存储在字典 per 中，键为题目序号（从 1 开始）
            per[j + 1] = str(t / stu * 100) + '%'
        j += 1
    # 将当前学生的得分添加到列表 scolst 中
    scolst.append(sco1)
    # 重置回答正确的总人数 t 为 0，用于下一个学生的统计
    t = 0

# 遍历每个学生的得分列表 scolst，输出每个学生的得分
for k in scolst:
    print(k)
# 输出每道题的正确率字典 per
print(per)
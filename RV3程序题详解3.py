# 从键盘获取输入的成绩字符串，按空格分割成列表
scores_str = input()
scores_list = list(map(int, scores_str.split()))

# 初始化等级人数统计的字典
grade_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}

# 遍历成绩列表，统计每个等级的人数
for score in scores_list:
    if 90 <= score <= 100:
        grade_count['A'] += 1
    elif 80 <= score < 90:
        grade_count['B'] += 1
    elif 70 <= score < 80:
        grade_count['C'] += 1
    elif 60 <= score < 70:
        grade_count['D'] += 1
    elif 0 <= score < 60:
        grade_count['E'] += 1

# 计算总人数
total_count = len(scores_list)

# 计算总分
total_score = sum(scores_list)

# 计算平均分，保留两位小数
average_score = round(total_score / total_count, 2) if total_count > 0 else 0

# 输出等级人数统计的字典
print(grade_count)

# 输出总人数和平均分
print(f"总人数为：{total_count}，平均分为：{average_score}")
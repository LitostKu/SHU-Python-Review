# 从用户处获取输入的二进制字符串
a = input()
# 计算输入二进制字符串的长度
num = len(a)
# 初始化计数器 s 为 0，用于遍历二进制字符串
s = 0
# 初始化空字符串 total，用于存储翻译后的文本
total = ''

# 循环遍历二进制字符串，每次处理 8 位二进制数
while s < num:
    # 截取从索引 s 到 s + 8 的 8 位二进制字符串，并将其转换为十进制整数
    num1 = int(a[s:s + 8], 2)
    # 将十进制整数转换为对应的 ASCII 字符
    ans = chr(num1)
    # 计数器 s 增加 8，以便处理下一组 8 位二进制数
    s += 8
    # 将转换后的字符添加到 total 字符串中
    total += ans

# 输出翻译后的文本
print(total)

# 将翻译后的文本按空格分割成单词列表
lst = total.split()
# 计算单词列表的长度，即单词的总数
num2 = len(lst)

# 导入 random 模块，用于生成随机数
import random
# 初始化空列表 seq，用于存储 1 到单词总数之间的整数
seq = []
# 初始化计数器 i 为 0
i = 0
# 循环生成 1 到单词总数之间的整数，并添加到 seq 列表中
while i < len(lst):
    i += 1
    seq.append(i)

# 从 seq 列表中随机选择一个整数
n = random.choice(seq)
# 根据随机选择的整数 n，获取对应的单词
anse = lst[n - 1]

# 按照指定格式输出单词总数、随机数和对应的单词
print('一共有{}个单词，生成的随机数是{}，第{}个单词为{}'.format(num2, n, n, anse))




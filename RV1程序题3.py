a=input()
num=len(a)
s=0
total=''
while s<num:
    num1=int(a[s:s+8],2)
    ans=chr(num1)
    s+=8
    total+=ans
print(total)
lst=total.split()
num2=len(lst)
import random
seq=[]
i=0
while i<len(lst):
    i+=1
    seq.append(i)
n=random.choice(seq)
anse=lst[n-1]
print('一共有{}个单词，生成的随机数是{}，第二个单词为{}'.format(num2,n,anse))




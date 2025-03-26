dic1=eval(input())
totalnum=int(input())
i=0
dic2={v:r for r,v in dic1.items()}
s=[0,0,0,0,0]
dic={}
while i<totalnum:
    num=input()
    i+=1
    if num[-1].isupper():
        num=num[:-1]+'0'
    for j in dic1.values():
        if int(num[-1]) in j:
            key=dic2[j]
            s[key-1]=s[key-1]+1
            dic[key]=s[key-1]
print(dic)
    
            


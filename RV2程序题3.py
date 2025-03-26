stu,ques=input().split()
stu,ques=int(stu),int(ques)
sco=list(map(int,input().split()))
tw=list(map(int,input().split()))
per={}
t=0
sco1=0
scolst=[]
for i in range(0,stu+1):
    ans=list(map(int,input().split()))
    j=0
    while j < ques:
        if ans[j]==tw[j]:
            sco1+=sco[j]
            t+=1
            per[j]=str(t/stu)+'%'
        j+=1
        scolst.append(sco1)
for k in scolst:
    print(k)
print(per)
    

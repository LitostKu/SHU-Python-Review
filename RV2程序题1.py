flag=0
sum1=0
sum2=0
while flag==0:
    a=list(map(eval,input().split()))
    if a[-1]==0:
        flag=1
    if a[-1]==1:
        sum1+=a[0]
        
    if a[-1]==2:
        sum2+=a[0]
        
if sum1>=149:
            sum1=sum1-100
if sum2>=399:
            sum2=sum2-200
print('{:.2f}'.format(sum1+sum2))

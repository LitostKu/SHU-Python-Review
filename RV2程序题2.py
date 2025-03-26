m,n=input().split()
m,n=int(m),int(n)
s={'0':'零','1':'壹','2':'贰','3':'叁','4':'肆','5':'伍','6':'陆','7':'柒','8':'捌','9':'玖'}
flag=0
for i in range(m,n+1):
    if i%6==0:
        a=str(i)
        b=s[a[0]]
        c=s[a[1]]
        d=s[a[2]]
        if a[2]=='0' and a[1]=='0':
            print('{}佰'.format(b))
        if a[2]=='0' and a[1]!='0':
            print('{}佰{}拾'.format(b,c))
        if a[2]!='0' and a[1]!='0':
            print('{}佰{}拾{}'.format(b,c,d))
        if a[2]!='0' and a[1]=='0':
            print('{}佰零{}'.format(b,d))
    else:
        flag+=1
            
if flag==n-m+1:
    print('[{},{}]区间内无满足要求的数'.format(m,n))
    
        

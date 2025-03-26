f=open('sg.txt')
txt0=f.read().split('\n')

line1=txt0[0].split()
line2=txt0[1].split()
line3=txt0[2].split()
txt=line1+line2+line3
s=0
for i in txt:
    s+=int(i)
average=s/len(txt)
d=[]
for j in txt:
    if int(j)>average:
        d.append(j)
a=' '.join(d)
print(average)
print(a)
f.close
        
        
    



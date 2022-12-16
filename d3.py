x=list(map(int,input().split()))
x.sort()
m=max(x)
min=99
c=0
for i in x:
    if i>=0 and i<min:
        min=i
for i in range(min,m+1):
    if i in x:
        continue
    else:
        print(i)
        c=1
        break
if c==0:
    print(m+1)
    

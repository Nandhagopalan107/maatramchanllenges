a=list(map(int,input().strip().split()))
f=0
s=0
for i in a:
   ns=max(i+s,f)
   s=f 
   f=ns
print(f)
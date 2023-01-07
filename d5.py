def check(x):
    if x>=1 and x<=26:
        return 1
    return -1


x=input().strip()
c=0

#for single digit numbers
for i in x:
    if(check(int(i))==1):
        c+=1
        print(chr(64+int(i)),end="")
print()

#for 2 digit numbers
start=0;end=2
while(end<=len(x)):
    if(check(int(x[start:end]))==1):
        c+=1
        print(chr(64+int(x[start:end])))
    start+=1
    end+=1
print(c)

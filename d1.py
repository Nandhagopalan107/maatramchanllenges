x=list(map(int,input("Enter the list:").split()))
y=int(input("Enter the value of k:"))
f=0
for i in range(len(x)):
    if f==0:
        for j in range(i+1,len(x)):
            if(x[i]+x[j]==y):
                print(x[i],x[j])
                f=1
    else:
        break

if(f==0):
    print("No numbers")

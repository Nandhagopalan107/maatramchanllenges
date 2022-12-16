x=list(map(int,input("Enter the list:").split()))
y=[]
for i in range(len(x)):
    p=1
    for j in range(len(x)):
        if i!=j:
            p*=x[j]
    y.append(p)
print(y)
        
    

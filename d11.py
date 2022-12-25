x=input().strip()
k=int(input())
l=len(x)
ml=0;s=""
for i in range(l):
	for j in reversed(range(i+1,l+1)):
		str1=x[i:j]
		if len(set(str1))==k and len(str1)>ml:
			ml=len(str1)
			s=str1
print(s)


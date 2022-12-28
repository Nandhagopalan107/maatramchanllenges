"""
Given an array of int and a num k, where 1<=k<=len(array), compute the maximum values of 
each subarray of length k.
For ex, given array = [10,5,2,7,8,7] and k=3, we should get: [10,7,8,8] since:
		. 10 = max[10,5,2]
		. 7  = max[5,2,7]
		. 8  = max[2,7,8]
		. 8  = max[7,8,7]
"""
print("Enter the list: ")
x=list(map(int,input().split()))
y=int(input("Enter the size of subarrays:\n"))
m=[]
for i in range(len(x)-y+1):
	m.append(max(x[i:i+y]))
print(m)
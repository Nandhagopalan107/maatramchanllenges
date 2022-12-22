x=input("Enter the number: ").strip()
l=[int(i) for i in x]
s=0
for i in range(len(l)):
	s+=(l[i]**(i+1))
if s==int(x):
	print("Yes,%s is a Disarium number"%x)
else:
	print("No, %s is not a Disarium number"%x)



	"""
	135
	1**1 + 3**2 + 5**3 = 135
	The sum of the numbers that is obtained from raising the digits to its poision th power is equal to itself is known as disarium number"""
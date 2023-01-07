"""Highest Index (With a Twist)

Given a name, return the letter with the highest index in alphabetical order, with its
corresponding index, in the form of a string. You are prohibited to use max () nor is reassigning a value to the alphabet list allowed.

Examples
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "1",
alphabet_index(alphabet, "Flavio")-"22v"
alphabet_index(alphabet, " 0sca r^ prime prime ") -"19s"
"""
def max_letter(a):
	alpha="abcdefghijklmnopqrstuvwxyz"
	m=a[0]
	for i in range(1,len(a)):
		if m<a[i]:
			m=a[i] 
	for i in range(26):
		if(alpha[i]==m):
			print(str(i+1)+m)
			break
x=input().strip()
max_letter(x)
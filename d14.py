"""Given a sentence as txt, return True if any two adjacent words have this property: One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).
Examples
vowel_links("a very large appliance")
vowel_links("go to edabit") → True
vowel_links("an open fire") → False
vowel_links("a sudden applause") → False"""
x=input().strip()
l=x.split()
v="aeiou"
for i in range(1,len(l)):
	if l[i-1][-1] in v and l[i][0] in v:
		print("True")
		exit(0)
print("False")
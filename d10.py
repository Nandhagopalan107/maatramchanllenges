"""There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 5, then there are 8 unique ways:
1, 1, 1, 1,1
2, 1, 1, 1
1, 2, 1, 1
1, 1, 2, 1
1, 1, 1, 2
2, 2 ,1 
2, 1, 2
1, 2, 2

it is based on fibonacci sereis 
for n steps there is (n+1)th fibonacci number starting from 1

fibo - > 1 1 2 3 5 8 
"""

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

a = int(input("Enter no of steps : "))
print(fib(a+1),"ways to climb")
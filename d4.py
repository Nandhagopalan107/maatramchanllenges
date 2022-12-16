# i/p: 100000  o/p: 100,000
# i/p: 1000    o/p: 1,000
# i/p: 100     o/p: 100
def formatnum(n):
    l=len(n)
    m=""
    for i in range(1,l+1):
        if (i-1)%3==0 and i-1>0:
            m+=","
        m+=n[-i]
    print(m[::-1])
x=input().strip()
formatnum(x)

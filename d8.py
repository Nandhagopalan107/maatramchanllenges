l=list(input().split())
w=input().strip()
wl=len(w)
for i in l:
    if i[:wl]==w:
        print(i,end=" ")

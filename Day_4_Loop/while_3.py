n=int(input())
i=1
if i%2==0:
    n=n-1
else:
    n=n
while i<=n:
    print(i,end=" ")
    i=i+2
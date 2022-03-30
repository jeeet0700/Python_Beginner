n=int(input())
d=0
som=0
while n>0:
    d=n%10
    n=n//10
    som=som+d
print(som)
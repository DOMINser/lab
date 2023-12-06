import random
n=int(input())
n=n

a=[]
for i in range (0,n):
    k=random.randint(1,100)
    print(k)
    a.append(k)
print(a)
mx=a[0]
mn=a[0]
nmn=0
xmn=0
for i in range(0,len(a)):
    if mx<a[i] and mx!=a[i]:
        mx=a[i]
        xmn=i
    if mn>a[i] and mn!=a[i]:
        mn=a[i]
        nmn=i
a.insert(xmn,0)
a.insert(nmn+1,0)
print(mx,xmn,mn,nmn)
print(a)


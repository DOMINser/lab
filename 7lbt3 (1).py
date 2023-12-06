m=int(input())
n=int(input())
spis=[]
k=0
for i in range(0,n):
    k=str(input())
    spis.append(k)
print(spis)
spis1=[]
t=0
for c in range(0,m):
    spis1.append([])
    for i in range(0,n):
        spis1[t].append(spis)
    
    t+=1
for i in range(0,m):
    print(spis1[i])

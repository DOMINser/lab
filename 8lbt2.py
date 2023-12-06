def zd2():
    m=int(input())
    n=int(input())
    spis=[]
    t=0
    ch=0
    for i in range(0,m):
        spis.append([])
        for k in range(0,n):
            spis[t].append(str(input()))
        t+=1
    
    print(spis)

    for i in range(0,m):
        print(spis[i])
    
    if n==m:
        print("матрица квадратная")
    kl=0
    spis1=[]
    n1=n-1
    if n==m and n!=1 and m!=1:
        for i in range(0,m):
            for k in range(0,n):
                if i==k and int(spis[i][k])%2==0:
                    kl+=1 
                    spis1.append(spis[i][k])
                if n1==k and int(spis[i][k])%2==0:
                    kl+=1
                    spis1.append(spis[i][k])
            n1-=1
        print(kl,spis1)
    if (n==1) and (m==1) and (int(spis[0][0])%2==0):
        print(1)
zd2()

spis=[]
def prst():
    spis=[]
    for u in range(1,11):
        k=0 
        ch=int(input())   
        for i in range(1,11):
            if ch%i==0:
                k+=1
        if (ch<10 and k==2) or (ch>10 and k==1):      
            spis.append(ch)
    print(spis)

prst()

sp={'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'e','ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n','о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh','ц':'ts','ч':'ch','ш':'sh','щ':'shch','ъ':'ie','ы':'y','ь':'--','э':'e','ю':'iu','я':'ia'}
s='окунь'
s=list(s)
zp=[]
k=1
for i in range(len(s)):
    k=sp[s[i]]
    zp.append(k)
print(zp)
        

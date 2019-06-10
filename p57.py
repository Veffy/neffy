e,f=map(str,input().split())
g=0
for i in range(0,len(e)):
    for j in range(0,len(f)):
        if e[i]==f[j]:
            g=g+1
            #print(e[i],"==",f[j])
if g>=2:
    print("yes")
else:
    print("no")

n = (input())
l = len(n)
def bal(s):
    a = len(s)
    c = []
    for i in range(a+1):
        for j in range(a+1):
            if(j>i):
                d = s[i:j]
                if(d == d[::-1]):
                    if d not in c:
                        c.append(d)
    e=[]
    for i in c:
        e.append(len(i))
    f=max(e)
    g=e.index(f)
    h=c[g]
    return(len(h))
print(l-bal(n))

from random import randint

def maxYear(L):
    birth=sorted([ people[0] for people in L])
    death=sorted([ people[1] for people in L])
    n,l=0,[]
    for year in birth:
        n=n+1
        m=0
        while year>death[m]:
            m=m+1
        l.append(n-m)
    return(birth[l.index(max(l))])
        
def ranlist():
    L=[]
    for i in range(100):
        a=randint(1900,1999)
        L.append((a,randint(a,2000)))
    return(L)

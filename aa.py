from numpy import*
from random import*
def pos(c,n):
    q=""
    for i in range(n):
        for j in range(n):
            if c==m[i,j]:
                q=chr(ord("A")+i)+chr(ord("A")+j)
    return q
def remplir(n):
    ch="abcdefghijklmnopqrstuvwxyz0123456789"
    for i in range(n):
        for j in range(n):
            p=randint(0,len(ch)-1)
            m[i,j]=ch[p]
            ch=ch[:p]+ch[p+1:]
def creat(n,ch):
    dd=""
    for i in range(len(ch)):
        if ch[i]!=" ":
            dd=dd+pos(ch[i],n)
        else:
            dd=dd+" "
    return dd
def affich(n):
    for i in range(n):
        for j in range(n):
            print(m[i,j],end="|")
        print()
def remplir2(n,msgi,mdc):
    s=0
    for i in range(n):
        m2[0,i]=mdc[i]
    for i in range(1,n+1):
        for j in range(n):
            if s<len(msgi):
                m2[i,j]=msgi[s]
                s=s+1
            else:
                m2[i,j]=" "
def tri(n):
    ok=True
    while ok==True:
        ok=False
        for i in range(n-1):
            if m2[0,i]>m2[0,i+1]:
                for j in range(n+1):
                    aux=m2[j,i]
                    m2[j,i]=m2[j,i+1]
                    m2[j,i+1]=aux
                ok=True
def rempf(n):
    ch=""
    for i in range(n):
        for j in range(1,n+1):
            ch=ch+m2[j,i]
    return ch
def affichh():
    for i in range(7):
        for j in range(6):
            print(m2[i,j],end="|")
        print()
ch="promotion bac 2019"
n=6
m=array([[str]*n]*n)
remplir(n)
affich(n)
print()
print(ch)
print()
msgi=creat(n,ch)
m2=array([[str]*6]*7)
mdc="CHAISE"
remplir2(n,msgi,mdc)
print()
affichh()
tri(n)
print()
affichh()
msg=rempf(n)
print()
print(msg)
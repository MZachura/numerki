from array import *

def interpolation(Yn,Xn,x,n):
    Wn=0.0

    for i in range (0,n):
        p=1.0
        for j in range (0,n):
            if(i!=j):
                p=p*(x-Xn[j])/(Xn[i]-Xn[j])
        Wn=Wn+Yn[i]*p

    print("%.7e"%Wn)


n=int(input("podaj n: "))

x0=float(input("podaj dla jakiego x "))
Yn=[]
Xn=[]

for i in range(n):
    xi=float(input("x: "))
    Xn.append(xi)
    yi=float(input("y: "))
    Yn.append(yi)

interpolation(Yn,Xn,x0,n)

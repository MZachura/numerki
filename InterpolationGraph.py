from array import *
import matplotlib.pyplot as plt


def interpolation(Yn,Xn,x,n,Wn):
    for i in range (0,n):
        p=1.0
        for j in range (0,n):
            if(i!=j):
                p=p*(x-Xn[j])/(Xn[i]-Xn[j])
        Wn=Wn+Yn[i]*p
    return Wn


print("interpolation f(x)=x^(1/2)")
Wn=0.0
Wn1=[]
nax=1.5
x0=0.1
xz=0
x1=[]
n1=nax/x0
Yn1=[0,0.707106781,1.224744871]
Xn1=[0,0.5,1.5]
for i in range(int(n1+1)):
    Wn=interpolation(Yn1,Xn1,round(xz,2),3,0.0)
    Wn1.append(Wn)
    x1.append(xz)
    xz+=x0

Yn1=[]
for i in range(int(n1+1)):
    yi=pow(x1[i],(1/2))
    Yn1.append(yi)

print("interpolation f(x)=1/(x^2+1)")
Wn=0.0
Wn2=[]
Xn2=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
Yn2=[]
n=len(Xn2)
for i in range(n):
    yi=1/(pow(Xn2[i],2)+1)
    Yn2.append(yi)
x=-5
x2=[]
for i in range((n*2)-1):
    z2=0.5

    Wn=interpolation(Yn2,Xn2,x,11,0.0)
    Wn2.append(Wn)
    x2.append(x)
    x=x+z2
Yn2=[]
for i in range((n*2)-1):
    yi=1/(pow(x2[i],2)+1)
    Yn2.append(yi)

plt.plot(x2,Wn2, label="interpolation")
plt.plot(x2,Yn2, label="f(x)=1/x^2+1")
plt.legend()
plt.show()

plt.plot(x1,Wn1, label="interpolation")
plt.plot(x1,Yn1, label="f(x)=x^(1/2)")
plt.legend()
plt.show()

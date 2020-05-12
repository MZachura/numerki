#y” = - y, y(0) = 10, y' (0) = 0
#y(x) = 10 cos x
#h=16./80.0

import math
from array import *
def analitycznie(i,yan):
    yan.clear()
    x=0
    i=0
    while i <=20:
        yan.append(10*math.cos(x))
        print(x,yan[i])
        x+=(16.0/80)
        i+=1


def euler(h,i,x,y):
    x.clear()
    x.append(0)
    y.clear()
    y.append(1)
    while i <=20:
        y.append(y[i]+(-2*x[i]*y[i])*h)
        x.append(x[i]+h)
        i+=1



def rungegokutty(h,i,x,y):
    x.clear()
    x.append(0)
    y.append(1)
    while i<=20:
        k1=h*(-2*x[i]*y[i])
        k2=h*(-2*(x[i]+0.5*h)*(y[i]+0.5*k1))
        k3=h*(-2*(x[i]+0.5*h)*(y[i]+0.5*k2))
        k4=h*(-2*(x[i]+1.0*h)*(y[i]+1.0*k3))
        y.append(y[i]+(1.0/6.0)*(k1+2.0*k2+2.0*k3+k4))
        x.append(x[i]+h)
        i+=1

yan=[]
x=[]
yeu=[]
yrk=[]
h=(16.0/80.0)
i=0
#euler(h,i,x,yeu)
analitycznie(i,yan)
#rungegokutty(h,i,x,yrk)
#i=0
#print("xi:    |yan:        |yeu:        |yrk:")
#while i<=20:
#    print("%.2f   | "%x[i],"%.6f  | "%yan[i],"%.6f  | "%yeu[i],"%.6f"%yrk[i])
#    i+=1

#f(x)=dx/(1+2x) a=0 b=2
a=0
b=2
fa=1/(1+2*a)
fb=1/(1+2*b)
#trapezy: S=((b-a)/2)*(fa+fb)
S=((b-a)/2)*(fa+fb)
print("wzór trapezów: ",S)
#parabole: S=((b-a)/6)*(fa+4f((a+b)/2)+fb)
fab=1/(1+2*((a+b)/2))
S=((b-a)/6)*(fa+4*fab+fb)
print("wzór parabol: ",S)
#complextrapezy:    S=(1/2*(fa+fb)+sumfi)dx
n=10
dx=(b-a)/n
sumfi=0
i=dx
while(i<(b-dx)):
    sumfi+=1/(1+2*i)
    i=i+dx
S=(0.5*(fa+fb)+sumfi)*dx
print("wzór złożonych trapezów: ",S)

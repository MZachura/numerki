def power(x,y):
    a=1
    for i in range(y):
        a=a*x
    return a
def pierwiastkowanie(l,s,p):
    x_p=l
    print(x_p)
    for i in range(p):
        x_p=(((s-1.0)*x_p+(l/(power(x_p,(s-1)))))/s)
        print(x_p)



i=0
while (i<=0):
    a=float(input("podaj liczbe pierwiastkowana(>0): "))
    if(a>0):
        i+=1
    liczba=a
stopien=int(input("podaj stopien pierwiastka: "))
precyzja=int(input("podaj precyzje(ilosc iteracji): "))
pierwiastkowanie(liczba,stopien,precyzja)

from array import *

kstore = open("k.txt", "r")
vstore = open("v.txt","r")
Nb=[]
i=0
z=0
vline=vstore.readline()
v=vline.split(";")
v.remove("\n")
lv=len(v)
s=[0]*lv
wch=[0]*lv
wy=[0]*lv
licz=0
print("macierz sasiedztwa:")
for d in range(lv):
    Nb.insert(d,[0]*lv)

for kline in kstore:
    k=kline.split(",")
    k1=int(k[0])
    k2=int(k[1])
    s[k1]+=1
    s[k2]+=1
    wch[k2]+=1
    wy[k1]+=1
    for d in range(int(lv)):
        i+=1
        Nb[k1][k2]=1
        Nb[k2][k1]=-1

for r in Nb:
    for c in r:
        print(c,end = " ")
    print()
print()
for z in range(len(wch)):
    abs1=abs((int(wy[z])-int(wch[z])))
    if(wy[z]!=wch[z]):
        nie=1
    if(abs1==1):
        licz+=1


print()
print("stopien: ")
print(s)
print()
print("stopien wychodzacy: ")
print(wy)
print()
print("stopien wchodzacy: ")
print(wch)
print()
print("sciezka eulera: ")
if(licz>=2):
    print("graf nie jest poleulerowski,nie mozna utworzyc scierzki eulera")
    print(licz)
else:
    print("graf poleulerowski, mozna utworzyc scierzke eulera")
    print(licz)
print()
print("cykl eulera: ")
if(nie>0):

    print("w grafie nie jest mozliwe stworzenie cyklu eulera")
    print(nie)
else:
    print("w grafie mozna utworzyc cykl eulera")
    print(nie)



#macierz sąsiedztwa, tab 2 wymiarowa od ilości wierzchołków i zawiera krawędzie do tych wierzchołków, jak skierowany
# to 1 ->  a jak -1 to <- 0 to brak
#podać do programu v i k, a program wyrzuca listę sąsiedztwa,
#1. sąsiedzi i stopień
#2.scieżka cykl eulera









# Wn = 0 . 0 ;
# dla i := 1 do n wykonuj
# rozpocznij
# p = 1 . 0 ;
# dla j := 1 do n wykonuj
# rozpocznij
# jezeli i <> j wtedy
# p = p ∗ ( x − xj ) / ( xi − xj ) ;
# zakoncz
# Wn : = Wn + yi ∗ p ;
# zakoncz

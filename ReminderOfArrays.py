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
istp=[0]*lv
ostp=[0]*lv
calculate=0
print("neighbourhood matrix:")
for d in range(lv):
    Nb.insert(d,[0]*lv)

for kline in kstore:
    k=kline.split(",")
    k1=int(k[0])
    k2=int(k[1])
    s[k1]+=1
    s[k2]+=1
    istp[k2]+=1
    ostp[k1]+=1
    for d in range(int(lv)):
        i+=1
        Nb[k1][k2]=1
        Nb[k2][k1]=-1

for r in Nb:
    for c in r:
        print(c,end = " ")
    print()
print()
for z in range(len(istp)):
    abs1=abs((int(ostp[z])-int(istp[z])))
    if(ostp[z]!=istp[z]):
        no=1
    if(abs1==1):
        calculate+=1


print()
print("step: ")
print(s)
print()
print("outgoing step: ")
print(ostp)
print()
print("incoming step: ")
print(istp)
print()
print("euler's path: ")
if(calculate>=2):
    print("the graph is not Polemerian, no Eulerian path can be created")
    print(calculate)
else:
    print("a poleuler graph, euler path can be created")
    print(calculate)
print()
print("euler cycle: ")
if(no>0):

    print("it is not possible to create an euler cycle in a graph")
    print(no)
else:
    print("euler cycle can be created in a graph")
    print(no)



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

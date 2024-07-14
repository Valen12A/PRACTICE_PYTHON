import random

#from numpy import sort


t=(10,'5',3,1,'sena',[])   #llenar tuplas
t1=10,'5',3,1.5,'cide',(),
t2=1000,                   #añadir a la tupla
t3=(500,)                  #añadir a a tupla
print(type(t3))
#t1=(x for x in range(10))
print(type(t))
print(t)
print(t1)
# for x in t:
#     print(x)
print(t[:2])
print(t[2:])

my_tuple = (11, 104, 10, 1000) 
#print(sort(my_tuple))
#my_tuple.append(10000)    
my_tuple=my_tuple+(100,)
#del my_tuple[0]
#my_tuple[1] = -10
print(my_tuple)
print(len(my_tuple))
print(my_tuple+my_tuple)  #añade la misma tupla una vez mas. 
print(my_tuple*3)         #añade la tupla 3 veces

var = 123
t1 = (1,1,1,1,1,)
t2 = (2, )
t3 = (3, var)
t1, t2, t3 = t2, t3, t1
print(t1, t2, t3)

tam=random.randint(5,15)
t=()
for i in range(tam):
    n=random.randrange(100)         #llenar una atupla
    t+=(n,)

print(t)
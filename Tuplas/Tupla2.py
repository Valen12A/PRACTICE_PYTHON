import random



tam =random.randint(5, 15) 
t= ()
for i in range (tam):
    n = random.randrange (100)
    t += (n,)
    
print (t)

t1= (t,)
print (t,)
t2 = (t1,  )
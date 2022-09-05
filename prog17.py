# Using range(1,101), make three list, 
# one containing all even numbers
# one containing all odd numbers 
# One containing only prime numbers.

from math import sqrt
def checkprime(num):
    if num <2:
        return 0
    else:
        for i in range(2, int(sqrt(num))):
            if num %i == 0:
                return 0
    return 1



even_list=[]
odd_list=[]
prime=[]
for i in range(1,101):
    if i%2 ==0:
        even_list.append(i)
    elif i%2==1:
        odd_list.append(i)
    
        
        
for i in range(1,101):        
        if checkprime(i):
            prime.append(i)
                
print("even list",even_list)
print("odd list",odd_list)
print("prime",prime)
                
        
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
                
# 



 #From the two list obtained in previous question, make new lists, containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.
list1 = even_list + odd_list
list=[]
for i in list1:
    if i%2==0 or i%6==0 or i%8==0 or i%10 or i%3==0 or i%5==0 or i%7==0 or i%9==0:
        list.append(i)
        
print(list)
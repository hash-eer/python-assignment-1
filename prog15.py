#Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.
product=0
count=0
sum=0
n=0


while n!= 'q' or n!= 'Q':
    n=input("enter the number to perform operation and enter q to stop")
    if n == 'q':
        break;
    else:
        n=int(n)
        product=product*n
        sum=sum+n
        count=count+1
    
    
    
    
print("product of all the numbers is",product)
print("average of all the number is ",sum/(count-1))
    
    


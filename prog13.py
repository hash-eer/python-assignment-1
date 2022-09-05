# Take 10 integers from keyboard using loop and print their average value on the screen.


n=0
sum=0

for i in range(0,10):
    n=int(input("enter the number"))
    sum=sum+n
    
print("average value of the 10 numbers is",sum/10)
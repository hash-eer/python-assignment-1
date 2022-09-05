#Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish
count=0
sum=0
n=1
while n!=0:
    n=int(input(""))
    sum=sum+n
    count+=1
    
print("sum of the number is ",sum)
print("average of the numbers is",sum/(count-1))
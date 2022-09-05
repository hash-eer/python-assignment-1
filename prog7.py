# Write a Python program that counts the number of elements within a list that are greater than 30.

list=[1,2,3,4,5,6,7,8,9,11,12,13,14,15,30,40,45,50,55,60,65,70,100]
count =0
a=int(input("enter minimum range"))
b=int(input("enter maximum range"))
for i in list:
    if a<=i <=b:
        count=count+1
print(count)
    
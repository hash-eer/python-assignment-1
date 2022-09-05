#Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
list=[]
a = int(input("enter the number total number to make a list"))
for i in range(0,a):
    n=int(input("enter the numbers"))
    list.append(n)

i=0
element= int(input("enter the element to serach"))
for x in list:
    if(x==element):
        list.pop(i)
        i=i-1
        
    i=i+1

print(list)
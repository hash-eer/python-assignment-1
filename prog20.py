#You are given with a list of integer elements. Make a new list which will store square of elements of previous list.
list1=[1,2,3,4,5,6]
list2=[]
for i in list1:
    list2.append(i**2)
print(list1) 
print("square of this list is :",list2)
#Write a Python program to check a triangle is equilateral, isosceles or scalene.
#Note :
#An equilateral triangle is a triangle in which all three sides are equal.
#A scalene triangle is a triangle that has three unequal sides.
#An isosceles triangle is a triangle with two equal sides.

a,b,c=input("enter the three sides of the triangle").split()
if a==b==c: # if all are equal
    print("Equilateral triangle")
elif a==b or a==c or b==c : #if 2 are equal
    print("isosceles triangle")
else: 
    print("scalence triangle")

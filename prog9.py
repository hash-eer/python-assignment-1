#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user.
quantity=int(input("enter the quantity"))
cost=100
amount=quantity*cost
discount=0
if amount>1000:
    discount=amount*10/100
total=amount-discount
print("total cost for user id ",total)
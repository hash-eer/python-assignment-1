#  A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.
a=int(input("enter the number of class held"))
b=int(input("enter the class you have attended"))
#percentage=(a/b)*100
percentage=(b/a)*100
if percentage >=75:
    print("you are allowed to sit in the examination your attendance percentage is ", percentage)
else:
    print("you are not allowed to sit in the examination your attendance percentage is ", percentage)
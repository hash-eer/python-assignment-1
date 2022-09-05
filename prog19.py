#From a list containing ints, strings and floats, make three lists to store them separately
list=[1,2,3,4,5,6,"hi","bye","hello",1.2,2.3,4.5,5.6]
int_list=[]
string_list=[]
float_list=[]

for i in list:
    if type(i)==int:
        int_list.append(i)
    elif type(i)==float:
        float_list.append(i)
    elif type(i)==str:
        string_list.append(i)
        
print(int_list)
print(float_list)
print(string_list)
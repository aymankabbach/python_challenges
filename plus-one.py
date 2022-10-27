digits=[4,3,2,1]
def convert_array_to_string():
    num_st=""
    for num in digits:
        num_st+=str(num)
    return num_st
number=int(convert_array_to_string())+1
def convert_int_to_array():
    output=[]
    for n in str(number):
        output.append(n)
    return output
print(convert_int_to_array())
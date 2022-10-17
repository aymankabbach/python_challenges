def read_input():
    user_input=input("enter a number\n")
    return user_input
def is_input_number():
    user_input=read_input()
    try:
        user_input=int(user_input)
    except ValueError:
        return False
    else:
        return user_input
def get_number():
    wrong_input=True
    while wrong_input:
        user_input=is_input_number()
        if user_input!=False:
            return user_input
def is_number_even__or_odd(num):
    return num%2==0
def start():
    steps=0
    num=get_number()
    while num>0:
        even=is_number_even__or_odd(num)
        if even:
            num=num/2
        else:
            num-=1
        steps+=1
    return steps
print(start())
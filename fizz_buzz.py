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
def get_input():
    wrong_input=True
    while wrong_input:
        user_input=is_input_number()
        if user_input!=False:
            return user_input
        else:
            print("invalid input")
def FizzBuzz():
    number=get_input()
    array=[]
    for i in range(1,number+1):
        if i%3==0 and i%5==0:
            array.append("FizzBuzz")
        elif i%3==0:
            array.append("Fizz")
        elif i%5==0:
            array.append("Buzz")
        else:
            array.append(str(i))
    return array
def start():
    print(FizzBuzz())
start()

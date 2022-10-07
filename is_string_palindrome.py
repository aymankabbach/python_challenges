def read_input():
    user_input=input("enter a string\n")
    return user_input
def is_input_string():
    user_input=read_input()
    try:
        user_input=int(user_input)
    except ValueError:
        return user_input
    else:
        return False
def get_input():
    wrong_input=True
    while wrong_input:
        user_input=is_input_string()
        if user_input!=False:
            return user_input
        else:
            print("invalid input")
def convert_input_to_list(user_input):
    array=[letter for letter in user_input]
    return array
def convert_input_to_list_backword(user_input):
    array=[]
    x=-1
    if len(user_input)%2==0:
        while x>=-len(user_input)//2:
            array.append(user_input[x])
            x-=1
    else:
        while x>-len(user_input)//2:
            array.append(user_input[x])
            x-=1
    return array
def is_string_palindrome(array,array_backword):
    if array[0:(len(array)//2)]==array_backword:
        return True
    else:
        return False
def start():
    user_input=get_input()
    array=convert_input_to_list(user_input)
    array_backword=convert_input_to_list_backword(user_input)
    print(is_string_palindrome(array,array_backword))
start()
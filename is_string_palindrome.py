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
    array=[]
    for letter in user_input:
        array.append(letter)
    return array
def convert_input_to_list_backword(user_input):
    array=[]
    x=-1
    while x>=-len(user_input):
        array.append(user_input[x])
        x-=1
    return array
def is_string_palindrome(array,array_backword):
    if array==array_backword:
        return "palindrome"
    else:
        return "not palindrome"
def start():
    user_input=get_input()
    array=convert_input_to_list(user_input)
    array_backword=convert_input_to_list_backword(user_input)
    result=is_string_palindrome(array,array_backword)
    print(f"string is {result}")
start()
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
def convert_string_to_list(second_string):
    array=[letter for letter in second_string]
    return array
def check(first_string,second_string_array):
    for letter in first_string:
        if letter in second_string_array:
            second_string_array.remove(letter)
        else:
            return False
    return True
def start():
    first_string=get_input().lower()
    second_string=get_input().lower()
    second_string_array=convert_string_to_list(second_string)
    result=check(first_string,second_string_array)
    print(result)
start()
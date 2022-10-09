def read_input(message):
    user_input=input(f"{message}\n")
    return user_input
def is_input_number(message):
    user_input=read_input(message)
    try:
        user_input=int(user_input)
    except ValueError:
        return False
    else:
        return user_input
def get_input(message):
    wrong_input=True
    while wrong_input:
        user_input=is_input_number(message)
        if user_input!=False:
            return user_input
        else:
            print("invalid input")
def get_len_of_array():
    array_len=get_input("how many element you want to enter")
    return array_len
def create_array():
    array=[]
    for x in range(get_len_of_array()):
        number=get_input("enter a number")
        array.append(number)
    return array
def get_output(array):
    array_output=[]
    for element in array[len(array)//2:len(array)]:
        array_output.append(element)
    return array_output
def start():
    array=create_array()
    print(get_output(array))
start()
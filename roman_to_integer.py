letters_symbol=["I","V","X","L","C","D","M"]
letters_value=[1,5,10,50,100,500,1000]
def read_input():
    user_input=input("enter a Roman number\n")
    return user_input
def is_input_valid():
    user_input=read_input()
    for letter in user_input:
        if letter in letters_symbol:
            pass
        else:
            return False
    return user_input
def get_input():
    wrong_input=True
    while wrong_input: 
        user_input=is_input_valid()
        if user_input!=False:
            wrong_input=False
            return user_input
def get_letter_value(letter):
    letter_value=letters_value[letters_symbol.index(letter)]
    return letter_value
def compare_values(letter_value,next_letter_value):
    if letter_value<next_letter_value:
        return True
    else:
        return False
def convert(roman_number):
    global result
    position=0
    while position<len(roman_number):
        letter_value=get_letter_value(roman_number[position])
        if position+1<len(roman_number):
            next_letter_value=get_letter_value(roman_number[position+1])
            special_case=compare_values(letter_value,next_letter_value)
            if special_case:
                result+=next_letter_value-letter_value
                position+=1
            else:
                result+=letter_value
        else:
            result+=letter_value
        position+=1
    return result
def start():
    global result
    result=0
    roman_number=get_input()
    print(convert(roman_number))
start()
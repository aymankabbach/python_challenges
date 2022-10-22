numbers = {
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz"
}
number="299"
def is_number_one_digit():
    if len(number)==1:
        return True
    else:
        return False
def solution_one():
    output=[]
    for num in numbers[number]:
        output.append(num)
    return output
def split_number():
    array=[]
    for num in number:
        array.append(int(num))
    return array
def get_letters(array):
    letters_array=[]
    for number in array:
        if number==0 or number==1:
            pass
        else:
            letters_array.append(numbers[f"{number}"])
    return letters_array
def get_number_of_elements(letters_array):
    elements_number=1
    for element in letters_array:
        elements_number*=len(element)
    return elements_number
def get_number_elements(letters_array):
    elements=[]
    for element in letters_array:
        elements.append(0)
    return elements
def fill_in_output_array(elements_number,letters_array,elements):
    output=[]
    for number in range(elements_number):
        string=""
        X=-1
        for x in range(len(letters_array)):
            string+=letters_array[x][elements[x]]    
        elements[X]+=1
        while elements[X]>len(letters_array[X])-1:
            elements[X]=0
            elements[X-1]+=1
            X-=1
            if X==-len(letters_array):
                break
        X=-1
        output.append(string)
    return output
def solution_two():
    array=split_number()
    letters_array=get_letters(array)
    elements_number=get_number_of_elements(letters_array)
    elements=get_number_elements(letters_array)
    output=fill_in_output_array(elements_number,letters_array,elements)
    return output
def start():
    if number=="":
        print([])
    else:
        len_number=is_number_one_digit()
        if len_number:
            print(solution_one())
        else:
            print(solution_two())
start()
##You are given a binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). 
#The soldiers are positioned in front of the civilians. 
#That is, all the 1's will appear to the left of all the 0's in each row.

#A row i is weaker than a row j if one of the following is true:

#The number of soldiers in row i is less than the number of soldiers in row j.
#Both rows have the same number of soldiers and i < j.
#Return the indices of the "number_of_output" weakest rows in the matrix ordered from weakest to strongest.
from matplotlib.bezier import find_bezier_t_intersecting_with_closedpath


mat=[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

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
def get_number_of_output():
    global mat
    wrong_input=True
    while wrong_input:
        user_input=is_input_number()
        if user_input==False or user_input>len(mat):
            print("invalid input")
        else:
            return user_input
def get_number_of_soldiers():
    global mat
    rows_soldiers=[]
    row=0
    for array in mat:
        n_soldiers=0
        for element in array:
            if element==1:
                n_soldiers+=1
        rows_soldiers.append([row,n_soldiers])
        row+=1
    return rows_soldiers
def get_output(rows_soldiers,array):
    global mat
    output_array=[]
    while len(output_array)<len(mat):
        element_found=False
        for element in rows_soldiers:
            if element[1]==array[0] and element[0] not in output_array and element_found==False:
                element_found=True
                output_array.append(element[0])
                rows_soldiers.remove(element)
                array.pop(0)
    return output_array
def print_output(number_of_output,rows_soldiers,array):
    output=get_output(rows_soldiers,array)
    return output[:number_of_output]
def start():
    number_of_output=get_number_of_output()
    rows_soldiers=get_number_of_soldiers()
    array=[element[1] for element in rows_soldiers]
    array.sort()
    print(print_output(number_of_output,rows_soldiers,array))
start()

                




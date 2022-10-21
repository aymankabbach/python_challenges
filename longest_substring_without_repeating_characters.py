s="azertyzerfgtvb"
def convert_string_to_array():
    array=[letter for letter in s]
    return array
def get_array(arr,element):
    for letter in range(len(arr)):
        if arr[letter]==element:
            list=arr[letter+1:]
            return list
def start():
    array=convert_string_to_array()
    final_array=[]
    arr=[]
    for element in range(len(array)):
        if array[element] not in arr:
            arr.append(array[element])
        else:
            Array=[letter for letter in arr]
            final_array.append(Array)
            arr=get_array(arr,array[element])
            arr.append(array[element])
        if element==len(array)-1:
            final_array.append(arr)
    return final_array
def get_longest_array():
    longest=0
    final_array=start()
    for array in final_array:
        if len(array)>longest:
            longest=len(array)
    return longest
print(get_longest_array())
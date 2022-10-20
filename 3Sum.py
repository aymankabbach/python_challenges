nums=[-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
def get_the_distinct_triplets():
    array=[]
    for number in range(len(nums)-1):
            num=number+1
            for element in nums[num:]:
                value=0-(nums[number]+nums[num])
                if value in nums[num:] and nums.index(value)!=number and nums.index(value)!=num:
                    arr=[nums[number],nums[num],value]
                    if arr not in array:
                        array.extend([arr])
                num+=1
    return array
def is_combination_already_exist(array):
    to_remove=[]
    for element in range(len(array)-1):
        next_element=element+1
        for combination in array[next_element:]:
            element_found=0
            index=[]
            for number in range(len(array[element])):
                if array[element][number] not in combination:
                    break
                else:
                    for num in range(len(combination)):
                        if array[element][number]==combination[num] and num not in index:
                            element_found+=1
                            index.append(num)
                            break
            if element_found==3:
                to_remove.append(array[element])
                break
    return to_remove
def remove_existed_combinaition(array,to_remove):
    for element in to_remove:
        array.remove(element)
    return array
def start():
    array=get_the_distinct_triplets()
    to_remove=is_combination_already_exist(array)
    array=remove_existed_combinaition(array,to_remove)
    print(array)
start() 

nums=[3,4,5,7,8,8,8,10]
target=8
output=[]
f_output=[]
def target_not_in_nums():
        return [-1,-1]
def target_in_nums():
    index=nums.index(target)
    for number in range(len(nums[index::])):
        if nums[index::][number]==target:
            output.append(number+len(nums)-len(nums[index::]))
        else:
            break
def get_first_and_last_element():
    target_in_nums()
    f_output.extend([output[0],output[-1]])
    return f_output
if target not in nums or len(nums)==0:  
    print(target_not_in_nums())
else:
    print(get_first_and_last_element())
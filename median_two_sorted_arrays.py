nums1 = [1,2]
nums2 = [3,4]
def add_two_arrays():
    array=nums1+nums2
    return array
def sort_array():
    array=add_two_arrays()
    array.sort()
    return array
def start():
    array=sort_array()
    if len(array)%2==0:
        return float((array[int(len(array)/2)]+array[int((len(array)/2)-1)])/2)
    else:
        return float(array[int(len(array)/2)])
print(start())
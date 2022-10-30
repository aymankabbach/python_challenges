from matplotlib.artist import get


nums=[0,0,1,1,1,1,2,3,3]
def get_duplicates():
    counter=0
    to_remove=[]
    for  x in range(len(nums)-1):
        if nums[x]==nums[x+1] and counter>=1:
            to_remove.append(x)
        elif nums[x]==nums[x+1] and counter<1:
            counter+=1
        else:
            counter=0
    return to_remove
def remove_duplicates():
    to_remove=get_duplicates()
    for number in to_remove[::-1]:
        nums.remove(nums[number])
    print(nums)
remove_duplicates()
            
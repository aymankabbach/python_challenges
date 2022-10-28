nums1 = [1,2,3,0,0,0] 
m = 3 
nums2 = [2,5,6]
n = 3
for element in nums1[m:]:
    nums1.remove(element)
nums1+=nums2[0:n]
print(nums1.sort())
# Reverse the Array using recursion 

nums = [1,2,3,4,5,6,7,8,9]

def reverseList(nums,left,right):
    if left>=right:
        return
    
    nums[left],nums[right]=nums[right],nums[left]
    reverseList(nums,left+1,right-1)
  
    
reverseList(nums,0,8)
print(nums)
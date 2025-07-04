# Linear Search 

nums = [2,5,3,2,5,2,5,4,2,10]

def linear_search(nums ,target):
    n = len(nums)
    for i in range(0,n):
       if nums[i]==target:
           return i
       
    return -1 

print(linear_search(nums,4))  
           


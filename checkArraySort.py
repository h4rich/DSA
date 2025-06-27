# Check if Array or List is sorted

def is_sort(nums):
    n = len(nums)
    for i in range(0,n-1):
        if nums[i]>nums[i+1]:
            return False
            
    return True        
    
nums = [1,2,9,4,5,6,7]
print(is_sort(nums))
    
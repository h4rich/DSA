# Find the largest Element in Array and List

nums = [22,-78,45,100,44,99]

def largest_element():
    largest = nums[0]
    n = len(nums)
    for i in range(0,n):
        largest = max(largest,nums[i])

    return largest  
    
print(largest_element())
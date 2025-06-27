# find the second largest Element in Array and list

nums = [55,67,-45,66,98,88]

# Better Solution

def second_largest():
    largest = float("-inf")
    s_largest = float("-inf")
    n = len(nums)

    for i in range(0,n):
        largest = max(largest,nums[i])

    for i in range(0,n):
        if nums[i]>s_largest and nums[i]!=largest:
            s_largest = nums[i]

    return s_largest


# Optimal Solution

def second_largest():
    largest = float("-inf")
    s_largest = float("-inf")
    n = len(nums)

    for i in range(0,n):
        if nums[i]>largest:
            s_largest = largest
            largest = nums[i]

        elif nums[i]>s_largest and nums[i]!=largest:
            s_largest = nums[i]    

    return s_largest   


print(second_largest())

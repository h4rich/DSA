# Find Missing Number in Array

# Brute Solution 

nums = [9,6,4,2,3,5,7,0,1]

def missingNumber(nums):
    n = len(nums)
    for i in range(0,n+1):
        if i not in nums:
            return i


print(missingNumber(nums))





# Better Solution 

def missingNumber(nums):
    n = len(nums)
    freq = {}
    for i in range(0,n+1):
        freq[i]= 0

    for num in nums:
        freq[num] = 1

    for k,v in freq.items():
        if v ==0:
            return k


print(missingNumber(nums))





# Optimal Solution

def missingNumber(nums):
    n = len(nums)
    return  int(n*(n+1)/2 - sum(nums))


print(missingNumber(nums))


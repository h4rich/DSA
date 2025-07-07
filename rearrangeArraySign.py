# Rearranage Array Element by Sign 


# Brute Solution 

nums = [5,10,-3,-1,-10,6]

def arraySign(nums):
    pos = [5,10,6]
    nag = [-3,-1,-10]

    for i in range(0,len(pos)):
        nums[2*i] = pos[i]
        nums[(2*i)+1] = neg[i]

    return nums 

print(arraySign(nums))   






# Optimal Solution 

def arraySign(nums):
    n = len(nums)
    result = [0]*n
    posIndex = 0
    negIndex = 1

    for i in range(0,n):
        if nums[i]>=0:
            result[posIndex] = nums[i]
            posIndex+=2
        else:
            result[negIndex] = nums[i]
            negIndex +=2

    return result  


print(arraySign(nums))



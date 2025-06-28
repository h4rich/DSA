# Right rotate an Array by k place

#Brute solution 

nums = [3,9,5,6,7,2]

def rotate(nums,k):
    n = len(nums)
    rotation = k%n

    for _ in range(0,rotation):
        e = nums.pop()
        nums.insert(0,e)

    return nums 


print(rotate(nums,3))



# Better Solution (using slicing)

def rotate(nums,k):
    n = len(nums)
    k = k%n

    nums[:] = nums[n-k:]+nums[:n-k]

    return nums 

print(rotate(nums,3))





# Optimal Solution (using reverse)

nums = [3,9,5,6,7,2]

def reverse(nums,left,right):
   
    while left<right:
        nums[left],nums[right] = nums[right],nums[left]

        left+=1
        right-=1
    return nums

n = len(nums)
k=3

reverse(nums,n-k,n-1)
reverse(nums,0,n-k-1)
print(reverse(nums,0,n-1))           
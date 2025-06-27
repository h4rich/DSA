# Right rotate an Array by one place 

nums = [1,4,6,7,5,4,10]

n =len(nums)
temp = nums[n-1]

for i in range(n-2,-1,-1):
    nums[i+1]=nums[i]

nums[0] = temp

print(nums)
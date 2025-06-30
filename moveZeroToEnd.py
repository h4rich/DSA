# Move Zeros To End 

# Brute Solution 

nums  = [1,0,2,4,3,0,0,3,5,1]

n = len(nums)
temp =[]

for i in range(0,n):
    if nums[i]!=0:
        temp.append(nums[i])
        

nz = len(temp)
for i in range(0,nz):
    nums[i]= temp[i]
    
for i in range(nz,n):
    nums[i]=0

print(nums) 





# Optimal Solution

nums  = [1,0,2,4,3,0,0,3,5,1]

def move_zero(nums):
    n = len(nums)

    if n ==1:
        return
    
  
    i = 0
    while i<n:
        if nums[i]==0:
            break
        i+=1
    
    if i == n:
        return

    j=i+1
    while j<n:
        if nums[j]!=0:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
        j+=1
    
    return nums

   
print(move_zero(nums))    
    

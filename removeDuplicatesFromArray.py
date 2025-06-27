# Remove Duplicates from a sorted List

# Brute Solution 

nums = [1,1,1,2,2,3,4,4,5,7,7,9,10]

def remove_duplicates(nums):
    n = len(nums)
    freq_map = {}

    for i in range(0,n):
        freq_map[nums[i]]=0

    j = 0
    for k in freq_map:
        nums[i]=k
        j+=1

    return k

print(remove_duplicates(nums))  



# Optimal Solution


def remove_duplicates(nums):
    n = len(nums)
    if n==1:
        return 1
    
    i=0
    j=i+1
    while j<n:
        if nums[j]!=nums[i]:
            i+=1
            nums[i],nums[j]= nums[j],nums[i]

        j+=1
    return i+1        
    

print(remove_duplicates(nums))  



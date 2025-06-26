# sort a list using Selection Sort

def selection_sort(nums):
    n = len(nums)
    for i in range(0,n):
        min_index = i
        for j in range(i+1,n):
            if nums[j]<nums[min_index]:
                min_index = j

        nums[i],nums[min_index] = nums[min_index],nums[i]
    return nums
        
nums = [4,5,3,2,5,7,8]
print(selection_sort(nums))
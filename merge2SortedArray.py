# Merge 2 sorted array without duplicates

nums1 = [1,1,1,2,4,6,7]
nums2 = [1,2,3,6,7,8,9,10]

def mergeSortedArray(nums1,nums2):
    n = len(nums1)
    m = len(nums2)
    result = []
    i= 0
    j=0
    while i<n and j<m:
        if nums1[i]<=nums2[j]:
            if len(result) ==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i+=1
        else:
            if len(result) ==0 or result[-1]!=nums2[j]:
                result.append(nums2[j])
            j+=1

    while i<n:
            if len(result) ==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i+=1

    while j<m:
            if len(result) ==0 or result[-1]!=nums2[j]:
                result.append(nums2[j])
            j+=1        
    return result

print(mergeSortedArray(nums1,nums2))
    
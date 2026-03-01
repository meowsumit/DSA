# increasing order
def Bubb(nums):
    n = len(nums)
    for i in range(n - 2, -1, -1):
        is_swap = False
        for j in range(i + 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swap = True
        if is_swap == False:
            break
    return nums
nums = [2,3,4,1,5,6,7]
print (Bubb(nums))

# decreasing order
def Bubb(nums):
    n = len(nums)
    for i in range(n - 2, -1, -1):
        is_swap = False
        for j in range(i + 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swap = True
        if is_swap == False:
            break
    return nums
nums = [2,3,4,1,5,6,7]
print (Bubb(nums))
# increasing
class Solution:
    def select(self, nums):
        n = len(nums)
        for i in range(0, n):
            minValue = i
            for j in range(i + 1, n):
                if nums[j] < nums[minValue]:
                    minValue = j
            nums[minValue], nums[i] = nums[i], nums[minValue]
        return nums
nums = [1, 7 ,4 ,8 ,0 ,9 ,3]
obj = Solution()
print (obj.select(nums))

# reversed solution in increasing order
class Solution:
    def select(self, nums):
        n = len(nums)
        for i in range(n - 1, 0, -1):
            maxValue = i
            for j in range(i - 1, -1, -1):
                if nums[j] > nums[maxValue]:
                    maxValue = j
            nums[maxValue], nums[i] = nums[i], nums[maxValue]
        return nums
nums = [1, 7 ,4 ,8 ,0 ,9 ,3]
obj = Solution()
print (obj.select(nums))    

# reversed value decreasing order
class Solution:
    def select(self, nums):
        n = len(nums)
        for i in range(0, n):
            maxValue = i
            for j in range(i +1 , n):
                if nums[j] > nums [maxValue]:
                    maxValue = j
            nums[maxValue], nums[i] = nums[i], nums[maxValue]
        return nums
nums = [1, 7 ,4 ,8 ,0 ,9 ,3]
obj = Solution()
print (obj.select(nums))   
        
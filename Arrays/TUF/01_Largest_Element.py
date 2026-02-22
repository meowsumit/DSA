class Solution:
    def largestElement(self, nums):
        max_val = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
        
        return max_val
    
nums = [-3, -1, 2, 0, 3]

obj = Solution()

print(f"Largest element in the array is: {obj.largestElement(nums)}")


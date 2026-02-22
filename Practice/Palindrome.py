class Solution:
    def isPalindrome(self, n):
        num = n
        result = 0
        while num > 0:
            ld = num % 10
            result = ( result * 10 ) + ld
            num = num // 10
        return n == result

n = 1234
obj = Solution()
result = obj.isPalindrome(n)
print(result)

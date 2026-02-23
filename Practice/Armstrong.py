class Solution:
    def check_Armstrong(self, n):
        num = n
        total = 0
        p = len(str(n))
        while num > 0:
            ld = num % 10
            total = total + ld**p
            num = num // 10
        return n == total
n = 153
obj = Solution()
result = obj.check_Armstrong(n)
print(result)

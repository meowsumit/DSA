#ussing recursion

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1 or n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)

# n = 8
# print(fib(n))

def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    prev1 = 1
    prev2 = 1
    for i in range(3, n+1):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current
    return prev2
n = 8
print(fib(n))
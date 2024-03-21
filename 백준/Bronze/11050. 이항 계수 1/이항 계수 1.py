import sys
input = sys.stdin.readline
n, k = map(int,input().split())
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(factorial(n) // (factorial(k) * factorial(n - k)))
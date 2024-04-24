import sys
input = sys.stdin.readline

n = int(input())
arr = [1] * (n+1)
arr[1] = 2
for i in range(2, n+1):
    arr[i] = arr[i-2] + arr[i-1]
print(arr[n-1]%10007)
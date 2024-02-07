# 10773 제로

import sys

k=int(sys.stdin.readline())


stack = []
for i in range(k):
    n = int(sys.stdin.readline())
    if n != 0: stack.append(n)
    elif n == 0: stack.pop()

print(sum(stack))
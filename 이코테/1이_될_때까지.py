# -*- coding: utf-8 -*-
"""1이 될 때까지.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zlMHk8RlFCxlHT7FOJtW6Q2LJCJoo1Gd
"""

n, k = map(int, input().split())
ans = 0

while True:
    if n % k == 0:
        n //= k
        ans += 1
    else:
        n -= 1
        ans +=1

    if n == 1:
        break
print(ans)


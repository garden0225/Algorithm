n = int(input())
for i,j in sorted([input().split() for _ in range(n)], key = lambda x: (int(x[0]),int(x[1]))): print(i,j)
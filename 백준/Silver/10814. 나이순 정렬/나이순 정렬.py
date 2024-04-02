n = int(input())
arr = [input().split() for i in range(n)]
for i,j in sorted([[int(i),j] for i, j in arr], key = lambda x: x[0]):
    print(i,j)
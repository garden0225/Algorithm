n, k = map(int,input().split())
ans = [[] for _ in range(n)]

for i in range(0,n):
    for j in range(0,i+1):
        if i == 0 or j == 0 or j == i: # 첫 번째 행과 각 행의 약 끝 값 == 1 
            ans[i].append(1)
        else:
            ans[i].append(ans[i-1][j-1]+ans[i-1][j]) 

print(ans[n-1][k-1])
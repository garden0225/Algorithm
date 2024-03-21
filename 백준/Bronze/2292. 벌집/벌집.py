n = int(input()) # 
cnt = 1 
i = 1 # 벌집의 개수, 1부터 시작
while i < n: # 벌집의 수가 n보다 작을 때까지
    i += 6*cnt # 벌집의 수 = 벌집의 수 + 6*개수
    cnt+=1 # 할 때마다 개수 1 증가


print(cnt)
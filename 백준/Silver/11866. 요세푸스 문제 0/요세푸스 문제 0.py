#1158 요세푸스 문제
from collections import deque

n,k = map(int, input().split())
que =deque([])
result=[]
for i in range(1,n+1):
    que.append(i)

while que:
    for _ in range(k-1):
        que.append(que.popleft())
    result.append(que.popleft())

print(f"<{', '.join(map(str,result))}>")
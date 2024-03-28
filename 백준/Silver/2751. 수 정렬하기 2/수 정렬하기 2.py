import sys
n = int(sys.stdin.readline())

li = list({int(sys.stdin.readline()) for _ in range(n)})
# 정렬
li.sort()

# 출력
print(*li, sep='\n')
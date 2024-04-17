n = int(input())
dic = {}
for _ in range(n):
    a, b =input().split()
    dic[a] = b


for i,j in sorted(dic.items(), reverse=True):
    if j == "enter":
        print(i)
a, b = map(int, input().split())

li = [[i] * i for i in range(1, 50)]
li = sum(li,[])
print(sum(li[a-1:b]))
n, m = map(int, input().split())
arr = set([input() for _ in range(n)])
name = []
for i in range(m):
    i = input()
    if i in arr:
        name.append(i)
print(len(name),*sorted(name), sep='\n')
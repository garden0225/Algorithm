li = sorted([int(input()) for i in range(9)])
result = [[li[i], li[j]] for i in range(9) for j in range(i+1, 9) if sum(li)-li[i]-li[j] == 100]
for k in li:
    if k not in result[0]:
        print(k)

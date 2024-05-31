n = int(input())
for _ in range(n):
    arr = list(input())
    ans = 0
    ans2 = 0
    for i in arr:
        if i == "O":
            ans2 +=1
            ans += ans2
        else:
            ans2 = 0
    print(ans)
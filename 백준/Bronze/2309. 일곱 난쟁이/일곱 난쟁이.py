li = sorted([int(input()) for i in range(9)])
for i in range(9):
    for j in range(i+1,9):
        if sum(li)-li[i]-li[j] == 100:
            no_li = [li[i],li[j]] 
            break
for i in li:
    if i not in no_li:
        print(i)

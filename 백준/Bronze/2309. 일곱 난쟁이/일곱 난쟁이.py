li = sorted([int(input()) for i in range(9)]) # 9명의 난쟁이 정렬

for i in range(9): 
    for j in range(i+1,9):
        if sum(li)-li[i]-li[j] == 100: # 모든 합 - 2개의 값 < 작으면 
            remove1 = [li[i],li[j]] # 2개의 값들을 list 저장
    
for k in li:
    if k not in remove1:
        print(k)

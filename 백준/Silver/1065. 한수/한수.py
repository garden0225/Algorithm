N = int(input())

hansu = 0

for n in range(1, N+1):
    if n < 100: # 100 미만은 두 자리수이기 때문에 모두 한수
        hansu+=1
    if n >=100: # 100이상인 경우 1000이하인 경우  
        n = str(n)
        if int(n[1])-int(n[0]) == int(n[2])- int(n[1]):
            hansu+=1

print(hansu)

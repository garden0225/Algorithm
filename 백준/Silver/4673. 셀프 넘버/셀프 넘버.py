arr =  set(range(1,10001))
ans = set()

for i in range(1,10001):
    for j in str(i): # 숫자 i fㄹ str로 바꾸어 하나하나씩(j) 떼어준다
        i += int(j) # i 에 j를 더해준다 
    ans.add(i)

print(*sorted(arr-ans),sep='\n')
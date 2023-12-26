def solution(i, j, k):
    answer = 0
    for n in range(i,j+1):
        if str(k) in str(n):
            answer+=str(n).count(str(k)) # 11 때문에 숫자 n에서 k가 몇 개 있는지 카운트해야함
    return answer
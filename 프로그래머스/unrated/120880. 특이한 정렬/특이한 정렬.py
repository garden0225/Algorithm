def solution(numlist, n):
    answer =[i-n for i in numlist]
    
    result = [] # 정렬한 배열
    # 거리가 n에 가까운 순으로 정렬, 절댓값이 같으면 양수(= 큰 값) 먼저
    for i in sorted(answer[:], key=lambda x:[abs(x), -x]): 
        result.append(numlist[answer.index(i)])

    return result
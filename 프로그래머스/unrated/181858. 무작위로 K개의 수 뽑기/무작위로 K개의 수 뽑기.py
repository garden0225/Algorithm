def solution(arr, k):
    answer = []
    for i in arr:
        if len(answer) < k :
            if i not in answer:
                answer.append(i)
    for i in range(k):
        if len(answer) < k:
            answer.append(-1)
    return answer
def solution(n):
    answer = []
    for i in range(n):
        answer.append([0 for j in range(n)])

    for i in range(n):
        answer[i][i] = 1

    return answer
def solution(ineq, eq, n, m):
    if ineq == "<" :
        if eq =='=':
            answer = bool(n <= m)
        else:
            answer = bool(n < m)
    else:
        if eq == "=":
            answer = bool(n >= m)
        else:
            answer = bool(n > m)
    answer = int(answer)
    return answer
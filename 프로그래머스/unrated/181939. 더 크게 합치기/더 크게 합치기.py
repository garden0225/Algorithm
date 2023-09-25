def solution(a, b):
    answer = max(str(a)+str(b), str(b)+str(a))
    return int(answer)
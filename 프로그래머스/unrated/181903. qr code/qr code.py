def solution(q, r, code):
    answer = ''

    for i, string in enumerate(code):
        if i % q == r:
            answer+=string
    return answer
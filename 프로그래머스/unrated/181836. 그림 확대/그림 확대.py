def solution(picture, k):
    answer = []
    for i in picture:
        row = ''.join([j * k for j in i])
        answer.extend([row]*k)
    return answer
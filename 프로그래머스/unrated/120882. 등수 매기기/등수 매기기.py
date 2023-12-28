def solution(score):
    answer = [eng+mat for eng, mat in score]
    rank = sorted(answer, reverse = True)
    result=[rank.index(i)+1 for i in answer]
    return result
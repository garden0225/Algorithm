def solution(array):
    answer = [array.count(i) for i in array]
    max_count = max(answer)
    if answer.count(max_count) != max_count:
        return -1
    else:
        max_idx = answer.index(max_count)
        return array[max_idx]
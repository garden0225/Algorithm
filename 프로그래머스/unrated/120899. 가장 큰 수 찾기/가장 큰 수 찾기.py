def solution(array):
    answer = []
    return [(i,n) for n,i in enumerate(array) if i==max(array)][0]
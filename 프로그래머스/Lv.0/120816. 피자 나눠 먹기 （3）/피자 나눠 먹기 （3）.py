def solution(slice, n):
    result,mod = divmod(n,slice)
    if mod != 0: result+=1
    return result
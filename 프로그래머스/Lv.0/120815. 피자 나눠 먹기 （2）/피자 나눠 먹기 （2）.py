def solution(n):
    for i in range(6,6*n+1):
        if i%n == 0 and i%6 == 0:
            break 
    return i//6
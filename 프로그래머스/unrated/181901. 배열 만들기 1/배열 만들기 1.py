def solution(n, k):
    answer = []
    for i in range(1,n+1):
        if i%k==0:
            answer.append(i)
    return answer


#def solution(n, k):
#   return [i for i in range(k,n+1,k)]
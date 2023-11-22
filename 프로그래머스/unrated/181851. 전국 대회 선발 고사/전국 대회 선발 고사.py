def solution(rank, attendance):
    answer = []
    for n,i in enumerate(rank):
        if attendance[n]: answer.append([i,n])
    answer=sorted(answer,key=lambda v: v[0]) 
    return answer[0][1]*10000+answer[1][1]*100+answer[2][1]

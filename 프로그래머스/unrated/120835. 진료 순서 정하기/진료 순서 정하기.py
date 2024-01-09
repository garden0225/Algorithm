def solution(emergency):
    rank = sorted(emergency,reverse=True)
    result=[rank.index(i)+1 for i in emergency]
    return result 
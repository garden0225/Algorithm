def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)

#replace를 쓸려고 했는데 다 변환해서 실패 

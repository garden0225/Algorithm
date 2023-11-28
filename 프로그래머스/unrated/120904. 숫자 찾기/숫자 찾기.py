def solution(num, k):
    num= str(num)
    k= str(k)
    if k not in num:
        return -1
    else:
        for i in range(len(num)):
            if k==num[i]:
                return i+1
    
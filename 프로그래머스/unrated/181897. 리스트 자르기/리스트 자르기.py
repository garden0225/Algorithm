def solution(n, slicer, num_list):
    answer = []
    a,b,c = [int(i) for i in slicer]
    if n==1:
        return num_list[0:b+1]
    elif n==2:
        return num_list[a:]
    elif n==3:
        return num_list[a:b+1]
    else:
        return num_list[a:b+1:c]
    
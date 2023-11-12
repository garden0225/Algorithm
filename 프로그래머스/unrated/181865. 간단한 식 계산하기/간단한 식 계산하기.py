def solution(binomial):
    a = binomial.split()
    if a[1]=="+":
        return int(a[0])+int(a[2])
    elif a[1]=="-":
        return int(a[0])-int(a[2])
    else:
        return int(a[0])*int(a[2])
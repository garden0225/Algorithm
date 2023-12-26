def solution(sides):
    if sum(sides)-2*(max(sides)) > 0:
        return 1
    else: return 2

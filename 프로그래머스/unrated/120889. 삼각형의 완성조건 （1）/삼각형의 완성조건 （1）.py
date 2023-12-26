def solution(sides):
    return 1 if sum(sides)-2*(max(sides)) > 0 else 2

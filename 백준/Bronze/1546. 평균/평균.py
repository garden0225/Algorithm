n = int(input())
a = [*map(int, input().split())]
print(sum(i/max(a)*100 for i in a)/n)
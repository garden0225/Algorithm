t = int(input())
arr = [input() for i in range(t)]
for i in [i[::-1].split() for i in arr]:
    print(' '.join(i[::-1]))
import sys
n,m=map(int,input().split())
l=sys.stdin.readlines()
u={*l[:n]}&{*l[n:]}
print(len(u))
print(''.join(sorted(u)))
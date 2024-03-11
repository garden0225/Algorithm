a, b = map(int, input().split())
gcd = max(i for i in range(1,max(a,b)+1) if a % i == 0 and b % i ==0)
print(gcd)
print(int(a*b/gcd))   
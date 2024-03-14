N = int(input())  # 나누어지는 수
d = 2  # 나누는 수

while N != 1: # N이 1이 되기 전까지 반복
    if N % d != 0: # N이 d로 나누어 떨어져지지 않으면
        d += 1 # d + 1
    else:
        N //= d # N이 d로 나누어 떨어진다면 N을 d로 나눈 몫으로 갱신
        print(d)
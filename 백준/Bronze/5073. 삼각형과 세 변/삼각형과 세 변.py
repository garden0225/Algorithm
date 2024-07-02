while True:
    # 세 변의 길이를 입력받아 정렬
    a, b, c = sorted(map(int, input().split()))
    
    # 세 변의 길이의 합이 0인 경우 종료
    if a + b + c == 0:
        break
    
    # 삼각형 조건을 만족하지 못하는 경우
    if c >= a + b:
        print("Invalid")
    # 세 변의 길이가 모두 같은 경우
    elif a == b == c:
        print("Equilateral")
    # 두 변의 길이만 같은 경우
    elif a == b or b == c or c == a:
        print("Isosceles")
    # 세 변의 길이가 모두 다른 경우
    else:
        print("Scalene")
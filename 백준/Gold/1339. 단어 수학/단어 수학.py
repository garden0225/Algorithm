n = int(input())
li=[input() for _ in range(n)]
words = {} # 단어별 값을 지정
for i in li:
    for idx, j in enumerate(i[::-1]):
        if j not in words:
            words[j] = 10**idx
        else :
            words[j] += 10**idx
words = sorted(words.values(),reverse=True)
result = 0
num = 9
for k in words:
    result += k*num
    num -=1
print(result)
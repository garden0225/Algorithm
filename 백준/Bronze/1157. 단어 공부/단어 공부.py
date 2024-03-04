word = input().upper()
answer = {i: word.count(i) for i in set(word)}
result = [k for k, v in answer.items() if v == max(answer.values())]

print('?' if len(result) > 1 else result[0])

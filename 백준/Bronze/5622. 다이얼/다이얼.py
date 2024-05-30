dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
count = 0
for i in word:
    for j in dial:
        if i in j:
            count+=dial.index(j)+3
print(count)
c = int(input())
for _ in range(c): 
    li = [int(i) for i in input().split()]
    avg = sum(li[1:])/li[0]
    per = (sum(int(i> avg)  for i in li[1:])/li[0])*100
    print( "%0.3f%%" % per)
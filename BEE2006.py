c = int(input())
palpites = list(map(int, input().split()))

co = 0
for p in palpites:
    if p == c:
        co +=1
print(co)
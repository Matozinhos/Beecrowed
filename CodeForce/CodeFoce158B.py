import sys

n = int(sys.stdin.readline())
grupos = list(map(int,sys.stdin.readline().split()))

contagem = [0] * 5
for g in grupos: contagem[g] += 1

taxis = contagem[4] + contagem[3]
contagem[1] = max(0, contagem[1] - contagem[3])

taxis += contagem[2] // 2

if contagem[2] % 2 != 0:
    taxis += 1
    contagem[1] = max(0, contagem[1] - 2)

if contagem[1] > 0:
    taxis  += (contagem[1] + 3) // 4

print(taxis)
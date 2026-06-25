import sys
from itertools import combinations

while True:
    a = list(map(int, sys.stdin.readline().split()))
    if [0,0] == a:
        break

    N, B = a
    bolas = list(map(int, sys.stdin.readline().split()))
    check = [False] * (N + 1)
    check[0] = True
    
    for bola1, bola2 in combinations(bolas,2) :
        check[abs(bola1-bola2)] = True
            
    if check.count(True) == N + 1: print('Y')
    else: print('N')    
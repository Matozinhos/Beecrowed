import sys
b = set()
while True:
    a = list(map(int, sys.stdin.readline().split()))
    if [0,0] == a:
        break

    N, B = a
    bolas = list(map(int, sys.stdin.readline().split()))
    b.clear()
    
    for bola1 in range(len(bolas)):
        for bola2 in range(len(bolas) - bola1):
            b.add(abs(bolas[bola1 + bola2] - bolas[bola2]))
            
    if len(b) == N + 1: print('Y')
    else: print('N')
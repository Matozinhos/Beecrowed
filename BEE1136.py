import sys
b = set()

while True:
    a = list(map(int, sys.stdin.readline().split()))
    if [0,0] == a:
        break

    N, B = a
    bolas = list(map(int, sys.stdin.readline().split()))
    b.clear()

    for bola1 in bolas:
        for bola2 in bolas:
            b.add(abs(bola1 - bola2))

    if len(b) == N + 1: print('Y')
    else: print('N')
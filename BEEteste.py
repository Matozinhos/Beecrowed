# Area de Teste

import sys
import math

r = []

for _ in range(int(sys.stdin.readline())):
    c = list(sys.stdin.readline().split())
    
    n1, d1 = int(c[0]), int(c[2])
    n2, d2 = int(c[4]), int(c[6])

    match c[3]:
        case '+': 
            denominador = d1 * d2
            
            numerador = (denominador // d1 * n1) + (denominador // d2 * n2)

            mdc = math.gcd(numerador, denominador)
            
            num_simplificado = numerador // mdc
            den_simplificado = denominador // mdc

            r.append(f"{numerador}/{denominador} = {num_simplificado}/{den_simplificado}")
        case '-':
            denominador = d1 * d2

            numerador = (denominador // d1 * n1) - (denominador // d2 * n2)

            mdc = math.gcd(numerador, denominador)
            
            num_simplificado = numerador // mdc
            den_simplificado = denominador // mdc

            r.append(f"{numerador}/{denominador} = {num_simplificado}/{den_simplificado}")
        case '*':
            denominador = d1 * d2

            numerador = n1 * n2

            mdc = math.gcd(numerador, denominador)
            
            num_simplificado = numerador // mdc
            den_simplificado = denominador // mdc

            r.append(f"{numerador}/{denominador} = {num_simplificado}/{den_simplificado}")
        case '/':
            denominador = n2 * d1

            numerador = n1 * d2

            mdc = math.gcd(numerador, denominador)
            
            num_simplificado = numerador // mdc
            den_simplificado = denominador // mdc

            if denominador < 0:
                numerador = -numerador
                denominador = -denominador

            mdc = math.gcd(numerador, denominador)
            
            if mdc == 0: mdc = 1

            num_simplificado = numerador // mdc
            den_simplificado = denominador // mdc

            r.append(f"{numerador}/{denominador} = {num_simplificado}/{den_simplificado}")

for i in r: print(i)
#Escreva um algoritmo que leia quinze números informados pelo usuário e exiba a raiz quadrada de cada número

import math

for n in range(15):
    num = int(input("Número:"))
    resultado = math.sqrt(num)
    print(round(resultado, 2))
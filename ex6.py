#Criar um algoritmo que leia deznúmeros inteiros e informe o maior e o menor número.

num = int(input("Informe um número: "))
menor = num
maior = num

for n in range(9):
    num = int(input("Informe um número: "))
    if num > maior:
     maior = num
    if num < menor:
        menor =  num
print(f"Maior:{maior}")
print(f"Menor:{menor}")
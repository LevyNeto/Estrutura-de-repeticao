quantidade = 0
soma = 0
pares = 0

num = int(input("Digite um número (0 para parar): "))
maior = num
menor = num

while num != 0:
    quantidade = quantidade + 1
    soma = soma + num

    if num % 2 == 0:
        pares = pares + 1

    if num > maior:
        maior = num

    if num < menor:
        menor = num

    num = int(input("Digite um número (0 para parar): "))

media = soma / quantidade

print("Quantidade:", quantidade)
print("Média:", media)
print("Maior:", maior)
print("Menor:", menor)
print("Pares:", pares)
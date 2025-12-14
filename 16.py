n = 0
for i in range(10):
    a = int(input("Digite um numero"))
    if (a >= 0):
        n += 1
    else:
        n += 0
print(f" ao total, tem {n} numeros positivo")
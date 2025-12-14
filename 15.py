a = 0
contarPositivo = 0
while(a >= 0):
    a = int(input("Digite um numero"))
    if (a >= 0):
        contarPositivo += a
    else:
        print("Acabou")
print(f"A soma de tudo é {contarPositivo}")
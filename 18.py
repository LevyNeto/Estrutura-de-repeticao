opcao = 0

while opcao != 3:
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Sair")

    opcao = int(input("Escolha:"))

    if opcao == 1:
        a = int(input("Número 1:"))
        b = int(input("Número 2:"))
        print(a + b)

    if opcao == 2:
        a = int(input("Número 1:"))
        b = int(input("Número 2:"))
        print(a - b)
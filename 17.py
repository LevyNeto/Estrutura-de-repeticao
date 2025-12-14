pessoa = True
someIdades = 0
contPessoas= 0
while pessoa:
    pessoa = int(input("Digite a idade: "))
    someIdades += pessoa
    contPessoas += 1
media = someIdades / contPessoas
print(media)
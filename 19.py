a = int(input("Digite A: "))
b = int(input("Digite B: "))
for i in range(a + 1, b):
    if i % 2 != 0:
        print(i)
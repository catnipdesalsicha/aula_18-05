inicial = int(input("Digite o valor inicial: "))

resultado = 1

print("Sequência de valores de {}!:".format(inicial))

for i in range(inicial, 0, -1):
    resultado *= i
    print(i, end="")
    if i > 1:
        print(" * ", end="")

print(" = {}".format(resultado))
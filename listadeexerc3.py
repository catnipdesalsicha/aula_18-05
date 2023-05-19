valorn = 0
valorp = 0
cont=0
soma = 0
rep= "sim"

while rep == "sim":
    num = int(input("Digite um número: "))
    soma = num
    cont=cont+1
    if num > 0:
        valorp +=1
    elif num < 0:
        valorn += 1

    repeat = input("Continuar? (sim/não) ")

print((valorp)"números positivos e "(valorn)"números negativos.")
print("A média dos números é "(soma/cont))
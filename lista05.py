p = 0
impares = 0
somap = 0
soma = 0

num = int(input("Digite um número: "))

while num != 0:
    if num % 2 == 0:
        p += 1
        somap += num
    else:
        impares += 1

    soma += num

mediapares = somap / p 
mediageral = soma / (p + impares)
print('A média dos números pares é: {}'.format(mediapares))
print('A média de tudo é: {}'.format(mediageral))
print('Quantidade de números pares: {}'.format(p))
print('Quantidade de números ímpares: {}'.format(impares))

num = int(input("Digite um número: "))
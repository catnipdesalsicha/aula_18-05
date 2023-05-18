altmax=0
altminim=10

for i in range (0,15):
        altura=float(input("Digite a altura desejada: "))
        if altura>altmax:
                altmax=altura
        elif altura<altmax:
                altmax=altmax
        else:
                altura=altura

        if altura<altminim:
                altminim=altura
        elif altura<altminim:
                altminim=altminim
        else:
                altura=altura
        
        print("Sua altura máxima é: ", altmax, "Sua altura mínima é: ", altminim)
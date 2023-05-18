num=1
n1=0
n2=0
n3=0
n4=0

while num>0:
    num=int(input("Digite um número: "))
    if num>=0 and num<25:
        n1=n1+1
        print("0-25")
    elif num>=26 and num<50:
        n2=n2+1
        print("25-50")
    elif num>=51 and num<75:
        n3=n3+1
        print("51-75")
    elif num>=76 and num<=100:
        n4=n4+1
        print("76-100")

    print("A quantidade de números 0-25 é: ", n1, "A quantidade de números entre 26-50 é: ", n2, "A quantidade de números entre 51-75 é:", n3, "A quantidade de números ente 76-100 é: ", n4)
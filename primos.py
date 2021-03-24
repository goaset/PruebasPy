def primo(numero):
    contador = 0
    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            print(i)
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    numero = int(input("escirbe un numero: "))
    if primo(numero): #si es verdadero, python obvia la sintaxis  no se necesita poner == True
        print("si")
    else:
        print("no")


if __name__ == '__main__':
    run()
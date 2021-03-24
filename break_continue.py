def run():
    # for contador in range(1000): # imprime numeros pares
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000): # Recorre la variable hasta q llega a una cantidad especifica
    #     print(i)
    #     if i == 5798:
    #         break

    # texto = input("escribe: ") # imprime letras de un texto
    # for letra in texto:
    #     if letra == "o":
    #         break
    #     print(letra.upper())

    # inicio = 0
    # fin = int(input("cual quieres q sea el final de la cadena: "))
    # brk = int(input("quieres que termine antes?: "))
    # while inicio < fin:
    #     inicio += 1
    #     print(inicio)
    #     if inicio == brk:
    #         break
    inicio = 1
    fin = int(input("cual quieres q sea el final de la cadena: "))
    qst = input("quieres que termine antes (y/n) ")
    if qst == "y":
        brk = int(input("intresa la cantidad donde quieres que termin: "))
        while inicio <= fin:
            print(inicio)
            inicio += 1
            if inicio == brk:
                break
    else:
        while inicio <= fin:
            print(inicio)
            inicio += 1


if __name__ == '__main__':
    run()
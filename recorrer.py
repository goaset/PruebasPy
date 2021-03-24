def run():
#     name = input("Escribe tu nombre: ")
#     for letter in name:
#         print(letter)
# -------------------------------------- imprime letras de una fase
    cont = 0
    frase = input("escribe una frase: ")
    for caracter in frase:
        print(caracter.upper())
        cont += 1
        
    print ("La cantidad de letras son: " + str(cont))


if __name__ == '__main__':
    run()
''' # while imprime el numero 2 elevado n cantidad de veces con LIMITE
def run():
    LIMITE = 1000

    cont = 0
    pot2 = 2**cont
    while pot2 < LIMITE:
        print("2 elevado a " + str(cont) + " es igual a: " + str(pot2))
        cont = cont + 1
        pot2 = 2**cont

if __name__ == '__main__':
    run() '''

# for
# for cont in range(1, 1001): #el ciclo imprime numeros del 1 al 1000
#     print(cont)


# for i in range(1, 11): #el ciclo imprime la tabla del 11
#     print (11 * i)


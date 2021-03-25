# Crea un numero al azar entre 1 y 100 y te hace adivinar
import random #libreria para crear numeros random


def run():
    aleatorio = random.randint(1, 100)
    elige = int(input("Elige un numero entre 1 y 100: "))
    vidas = 5
    for i in range (1, vidas):
        vidas -= 1
        print("Te quedan " + str(vidas) + " vidas")
        if aleatorio == elige:
            print("Ganaste!!! XD")
            break
        if elige > aleatorio:
            elige = int(input("menos "))
        else:
            elige = int(input("MAS "))
    print(" YOU LOSE XC... Tu numero era " + str(aleatorio))
    
def whi(): 
    num_ale = random.randint(1,100) # crea numero random entre dos opciones 1 o 100
    num_ele = int(input("elige un numero entre 1 y 100: "))
    while num_ele != num_ale:
        if num_ele < num_ale:
            print("mas")
        else:
            print("menos")
        num_ele = int(input("elige otro: "))
    print("WIN!!!")
        


if __name__ == "__main__":
    run()
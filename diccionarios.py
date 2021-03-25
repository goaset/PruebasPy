def run():
    diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3,
    }
    # print(diccionario["llave1"])
    # print(diccionario["llave2"])
    # print(diccionario["llave3"])
    poblacion = {
        "Argentina": 444444,
        "Brasil": 555555,
        "Colombia": 666666, 
    }

    # for pais in poblacion.keys(): #Imprime los nombres de las llaves
    #     print(pais)
    # for pais in poblacion.values(): # imprime el contendio de las llaves
    #     print(pais)
    for pais, poblacion in poblacion.items(): #devuelve los nombres y contenido de las llaves
        print(pais + " tiene " + str(poblacion))

if __name__ == "__main__":
    run()
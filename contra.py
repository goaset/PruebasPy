import random

def generar():
    mayus = ["A", "B", "C", "D", "E", "F", "G"]
    minus = ["a", "b", "c", "e", "f", "g"]
    numero = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    simbolo = ["!", "#", "$", "%", "&"]

    caracteres = mayus + minus + numero + simbolo
    contrasena = []

    for i in range (15):
        caracteram = random.choice(caracteres)
        contrasena.append(caracteram)

    contrasena = "".join(contrasena) #convierte listas a str
    return contrasena

def run():
    contrasena = generar()
    print("Tu contrasena es: " + contrasena)


if __name__ == "__main__":
    run()

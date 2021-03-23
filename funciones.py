'''def imp_msj ():
    print("holi")
    print("mundo")

imp_msj()
'''

def conv(opcion):
    saludo = """
    Hola
    Amiguito
    Estas bn guapo!!!"""
    print(saludo + " El numero que elegiste fue " + opcion)

elige = str(input("Elige una opcion 1 2 3 : "))
if elige == "1":
    conv(elige)

elif elige == "2":
    conv(elige)

elif elige == "3":
    conv(elige)

else:
    print ("Guapo pero tonto")


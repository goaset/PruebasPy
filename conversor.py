'''pesos = input("cuanto pesos tienes: ")
pesos = float(pesos)
valordolar = input("tipo de cambio")
valordolar = float(valordolar)
dolar = pesos / valordolar
dolar = round(dolar, 2)
dolar = str(dolar)
valordolar = str(valordolar)  
var1 = 10

print("tienes $" + dolar + " Dolares, con tipo de cambio " + valordolar)

print(var1)'''


menu = """"
hola prro que quieres hacer

1 pesos

2 dolares

3 euro

otro numero? no hay acaso es usted idiota?
"""

seleccion = float(input(menu))
tc = float(input("Bien, ahora ingresa el tipo de cambio "))

if seleccion == 1:
    pesos = int(input("Ingrese la cantidad en pesos "))
    pesos = pesos * tc
    print(pesos)
elif seleccion == 2:
    dolar =  int(input("Ingrese la cantidad en dolares "))
    dolar = dolar * tc
    print(dolar)
elif seleccion == 3:
      euro = int(input("Ingrese la cantidad en euro "))
      euro = euro * tc
      print (euro)
else:
    print("usted esta idiota")


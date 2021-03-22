pesos = input("cuanto pesos tienes: ")
pesos = float(pesos)
valordolar = input("tipo de cambio")
valordolar = float(valordolar)
dolar = pesos / valordolar
dolar = round(dolar, 2)
dolar = str(dolar)
valordolar = str(valordolar)  
var1 = 10

print("tienes $" + dolar + " Dolares, con tipo de cambio " + valordolar)

print(var1)


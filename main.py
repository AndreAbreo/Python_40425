from  entrega2.cliente import *

cliente1 = Cliente("Juan", "Diaz", "CI:3.333.444-9", 1000)
cliente2 = ClienteVIP("Pedro", "Gomez", "CI:3.555.555-5", 5000, 20)

print(cliente1)
print(cliente2)

puntos_gastados = 500

print(f"{cliente1.nombre} gastó {puntos_gastados} puntos. Puntos restantes: {cliente1.gastar_puntos(puntos_gastados)}.")
print(f"{cliente2.nombre} gastó {puntos_gastados} puntos. Puntos restantes: {cliente2.gastar_puntos(puntos_gastados)}.")
#Autor: André Abreo
import csv
import os

salto = "\n"

def cargar_usuarios():
    with open('mi_db.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            usuarios[row[0]] = row[1]

def guardar_usuarios():
    with open('mi_db.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for usuario, password in usuarios.items():
            writer.writerow([usuario, password])

usuarios = {}
cargar_usuarios()

print("PROGRAMA DE REGISTRO por ANDRÉ ABREO")
print(salto)
while True:
    usuario = input(f"Registrar nombre de usuario: ")
    if usuario in usuarios:
        print(f"Este nombre de usuario ya existe. Por favor ingrese un nombre de usuario diferente.")
    else:
        password = input("Ingrese una contraseña: ")
        usuarios[usuario] = password
        print(f"Usuario '{usuario}' agregado exitosamente.")
        break
        print(salto)

guardar_usuarios()

print(salto)
print("LOGIN DE USUARIO")
intentos = 0
validacion = False
while not validacion and intentos < 3:
    usuario = input(f"Ingrese un nombre de usuario: ")
    password = input("Ingrese contraseña: ")
    if usuario in usuarios and usuarios[usuario] == password:
        validacion = True
        print(f"Ingreso exitoso.")
    else:
        intentos += 1
        if intentos < 3:
            print("Nombre de usuario o contraseña incorrectos. Intente de nuevo.")
        else:
            print(f"Ha excedido el número máximo de intentos.")

print(salto)           

print("Base de Datos")
f = open('mi_db.csv', 'r')
content = f.read()
print(content)
f.close()

print(salto)
print("Gracias por registrarse. ¡Hasta luego!")
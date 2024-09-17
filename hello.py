#Mensaje de bienvenida
nombre = input("Ingresa tu nombre: ")

def saludar(nombre):
    print(f"¡Hola, bienvenido {nombre}")

saludar(nombre)

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

def suma(num1, num2):
    suma=num1+num2
    print("La suma es:",suma)

def resta(num1, num2):
    resta=num1-num2
    print("La resta es:",resta)

suma(num1,num2)
resta(num1, num2)
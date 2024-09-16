#Mensaje de bienvenida
nombre = input("Ingresa tu nombre: ")

#Función de saludar
def saludar(nombre):
    print(f"¡Hola, bienvenido {nombre}")

saludar(nombre)

#Suma de 2 numeros
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

#Función de la suma de numeros
def suma(num1, num2):
    suma=num1+num2
    print("La suma es:",suma)

suma(num1,num2)
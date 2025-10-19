# 1. Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

# primerNumero = int(input('Introduce el valor del primer número: '))
# segundoNumero = int(input('Introduce el valor del segundo número: '))

# for valor in range(primerNumero, segundoNumero + 1): # Con el +1 hacemos que incluya el segundo numero.
#     if valor % 2 == 0:
#         print(valor)


# 2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.

import random


mayoresCero = 0
menoresCero = 0
igualesCero = 0

cantidadNumeros = int(input('Introduce la cantidad de valores que desea introducir: '))

for valor in range(cantidadNumeros):
    numeroIntroducido = int(input(f'Introduce el valor número {valor}: '))

    if numeroIntroducido > 0:
        mayoresCero += 1
    elif numeroIntroducido < 0:
        menoresCero += 1
    else:
        igualesCero += 1

print(f'Ha introducido {mayoresCero} valores mayores de 0, {menoresCero} valores menores de 0 y {igualesCero} valores iguales a 0.')


# 3. Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.

numeroAAdivinar = random.randint(1, 100)

for intento in range(10):
    numeroUsuario = int(input("Introduzca su número: "))

    if numeroUsuario == numeroAAdivinar:
        print('Ha adivinado el número en el intento ', intento)
    elif numeroUsuario > numeroAAdivinar:
        print('El número a adivinar es menor a ', numeroUsuario)
    else:
        print('El número a adivinar es mayor a ', numeroUsuario)


# 4. Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
#
# A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine el programa dará las siguientes informaciones:
#
# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# Informa si hemos introducido algún número igual a los límites del intervalo.

limite_inferior = int(input('Introduce el límite inferior: '))
limite_superior = int(input('Introduce el límite superior: '))

suma_valores_dentro_intervalo = 0
numeros_fuera_intervalo = 0
repeticion_limite_superior = False
repeticion_limite_inferior = False

while limite_inferior > limite_superior:
    print('El límite inferior no puede ser mayor al superior!')
    limite_inferior = int(input('Introduce el límite inferior: '))
    limite_superior = int(input('Introduce el límite superior: '))

valores = 1

while valores != 0:
    valores = int(input('Introduce un valor, o pulse 0 para salir: '))

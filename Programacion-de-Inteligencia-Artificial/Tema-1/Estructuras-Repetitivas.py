import random

# 1. Escribir un programa que imprima todos los números pares entre dos números que se le pidan al usuario.

# primerNumero = int(input('Introduce el valor del primer número: '))
# segundoNumero = int(input('Introduce el valor del segundo número: '))

# for valor in range(primerNumero, segundoNumero + 1): # Con el +1 hacemos que incluya el segundo numero.
#     if valor % 2 == 0:
#         print(valor)


# # 2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.



# mayoresCero = 0
# menoresCero = 0
# igualesCero = 0

# cantidadNumeros = int(input('Introduce la cantidad de valores que desea introducir: '))

# for valor in range(cantidadNumeros):
#     numeroIntroducido = int(input(f'Introduce el valor número {valor}: '))

#     if numeroIntroducido > 0:
#         mayoresCero += 1
#     elif numeroIntroducido < 0:
#         menoresCero += 1
#     else:
#         igualesCero += 1

# print(f'Ha introducido {mayoresCero} valores mayores de 0, {menoresCero} valores menores de 0 y {igualesCero} valores iguales a 0.')


# 3. Crea una aplicación que permita adivinar un número. La aplicación genera un número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido, además de los intentos que te quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número que había generado.

LOWER_VALUE = 1
MAX_VALUE = 100
MAX_TRIES = 10

random_number = random.randint(LOWER_VALUE, MAX_VALUE)

for tries in range(1, MAX_TRIES+1):
    numeroUsuario = int(input(f"Intento: {tries}. Introduzca un número del 1 al 100: "))

    if numeroUsuario == random_number:
        print('Ha adivinado el número en el intento ', tries)
        break
    elif numeroUsuario > random_number:
        print('El número a adivinar es menor a ', numeroUsuario)
    else:
        print('El número a adivinar es mayor a ', numeroUsuario)
    
    if tries == MAX_TRIES:
        print(f'Lo siento, el numero a acertar era el {random_number}')


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
repeticion_limite = False

while limite_inferior > limite_superior:
    print('El límite inferior no puede ser mayor al superior!')
    limite_inferior = int(input('Introduce el límite inferior: '))
    limite_superior = int(input('Introduce el límite superior: '))

valor = 1

while valor != 0:
    valor = int(input('Introduce un valor, o pulse 0 para salir: '))

    if valor == limite_inferior or valor == limite_inferior:
        repeticion_limite = True
    elif valor > limite_superior or valor < limite_inferior:
        numeros_fuera_intervalo += 1
    else:
        suma_valores_dentro_intervalo += valor

print(f'La suma de los valores de dentro del intervalo es: {suma_valores_dentro_intervalo}.')
print(f'Ha introducido {numeros_fuera_intervalo} {'valores' if numeros_fuera_intervalo > 1 else 'valor'} fuera del intervalo.')
print(f'{'Ha' if repeticion_limite else 'No ha'} introducido algun valor igual al límite.')


# 5. Crea un programa que pida un número por teclado al usuario y diga si es primo. En caso de que no se introduzca un número o que esta sea menor que 2 se debe mostrar un mensaje de error.

numero_a_evaluar = input('Introduce un numero a evaluar: ')

es_primo = True

if numero_a_evaluar.isdigit() and int(numero_a_evaluar) > 2:
    numero_a_evaluar = int(numero_a_evaluar)
    for divisor in range(2, numero_a_evaluar):
        if numero_a_evaluar % divisor == 0:
            es_primo = False

    print(f'El numero {numero_a_evaluar} {'es' if es_primo else 'no es'} primo')
else:
    print("El valor introducido debe tratarse de un número y ser mayor que 2")


# 6. Crea un programa que muestre en pantalla los N primeros número primos. El valor de N se pide por teclado al usuario/a.

cantidad_numeros_primos = int(input('Introduce la cantidad de números primos que desea mostrar: '))

contador_numeros = 0
numero_a_comprobar = 2

print(f'Los primeros {cantidad_numeros_primos} números primos corresponden a: ')

while contador_numeros <= cantidad_numeros_primos:
    no_es_primo = False
    for divisor in range(2, numero_a_comprobar):
        if numero_a_comprobar % divisor == 0:
            no_es_primo = True

    if not no_es_primo:
        print(numero_a_comprobar)
        contador_numeros += 1

    numero_a_comprobar += 1

# 7. Crea un programa que nos permita calcular la cuota de una hipoteca y su tabla de amortización después de que se pida al usuario/a:
#
# Importe del préstamo.
# La tasa de interés anual.
# Y el plazo de pago en años.

importe_prestamo = int(input('Introduce la cantidad de importe préstamo: '))
tasa_interes = (int(input('Introduce la tasa de interés anual en %: ')) / 100)
total_plazo_pagos = (int(input('Introduce el plazo de pago en años: ')) * 12)

tipo_interes_periodo = tasa_interes / 12

cuota_periodica = importe_prestamo * (tipo_interes_periodo / (1 - ((1 + tipo_interes_periodo) ** (-total_plazo_pagos))))

for mes in range(1, total_plazo_pagos + 1):
    interes = importe_prestamo * tipo_interes_periodo
    amortizado = cuota_periodica - interes
    importe_prestamo = importe_prestamo - amortizado
    print(f'Mes {mes}: Interes: {round(interes, 2)}, Amortizado: {round(amortizado, 2)}')
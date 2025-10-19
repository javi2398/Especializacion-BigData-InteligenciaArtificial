# 1. Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.

import math


primeraEdad = int(input('Introduce la edad de la primera persona: '))
segundaEdad = int(input('Introduce la edad de la segunda persona: '))

if primeraEdad == segundaEdad:
    print('Ambas personas tienen la misma edad')
elif primeraEdad > segundaEdad:
    print('La segunda persona es más joven.')
else:
    print('La primera persona es más joven.')


# 2. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
# Si se cumple Pitágoras entonces es triángulo rectángulo
# Si sólo dos lados del triángulo son iguales entonces es isósceles.
# Si los 3 lados son iguales entonces es equilátero.
# Si no se cumple ninguna de las condiciones anteriores, es escaleno.

lado1 = int(input('Introduce la medida del primer lado: '))
lado2 = int(input('Introduce la medida del segundo lado: '))
lado3 = int(input('Introduce la medida del tercer lado: '))

medidasTriangulo = [lado1, lado2, lado3]

medidasOrdenadas = sorted(medidasTriangulo)

calculoHipotenusa = math.sqrt(pow(medidasOrdenadas[0], 2) + pow(medidasOrdenadas[1], 2))

if calculoHipotenusa == medidasOrdenadas[2]:
    print('Se trata de un triángulo rectángulo')
elif lado1 == lado2 and lado2 == lado3:
    print('Se trata de un triángulo equilátero.')
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print('Se trata de un triángulo isósceles.')
else:
    print('Se trata de un triángulo escaleno.')


# 3. Escribir un programa que lea un año indicar si es bisiesto (un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400).

anyoAComprobar = int(input("Introduce el año que desea comprobar si es bisiesto: "))

if anyoAComprobar % 4 == 0:
    if anyoAComprobar % 100 == 0:
        if anyoAComprobar % 400 == 0:
            print(f'El año {anyoAComprobar} es bisiesto')
        else:
            print(f'El año {anyoAComprobar} no es bisiesto')

    print(f'El año {anyoAComprobar} es bisiesto')
else:
    print(f'El año {anyoAComprobar} no es bisiesto')


# 4. Escribir un programa que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros. Hay billetes de 500, 200, 100, 50, 20, 10 y 5€ y monedas de 2 y 1€.

cantidad_a_desglosar = int(input('Introduce la cantidad que desea desglosar: '))

cambio_disponible = [500, 200, 100, 50, 20, 10, 5, 2, 1]

print(f'{cantidad_a_desglosar} euros corresponderia a un cambio de: ')

for cambio in cambio_disponible:
    total_cambio = cantidad_a_desglosar // cambio
    cantidad_a_desglosar = cantidad_a_desglosar % cambio

    if total_cambio > 0:
        if cambio > 2:
            print(f"{total_cambio} {'billetes' if total_cambio > 1 else 'billete'} de {cambio} euros")
        else:
            print(f"{total_cambio} {'monedas' if total_cambio > 1 else 'moneda'} de {cambio} euros")


#5. Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.

dias_de_la_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

dia_introducido = 0

while dia_introducido < 1 or dia_introducido > 7:
    dia_introducido = int(input("Introduzca el dia de la semana: "))

print(f'El número {dia_introducido} corresponde al {dias_de_la_semana[dia_introducido - 1]}')


#6. Realiza un programa que pida tres números enteros y diga cuál es el mayor. No se puede usar la función max().

numeros_a_comprobar = []
numeros_a_comprobar.append(int(input('Introduzca el primer número: ')))
numeros_a_comprobar.append(int(input('Introduzca el segundo número: ')))
numeros_a_comprobar.append(int(input('Introduzca el tercer número: ')))

numeros_a_comprobar.sort()

print(f'El número más grande es el {numeros_a_comprobar[-1]}.')


# 7. Realiza un programa que pida cinco números enteros y diga cuál es el mayor No se puede usar la función max()..

numeros_a_comprobar2 = []
numeros_a_comprobar2.append(int(input('Introduzca el primer número: ')))
numeros_a_comprobar2.append(int(input('Introduzca el segundo número: ')))
numeros_a_comprobar2.append(int(input('Introduzca el tercer número: ')))
numeros_a_comprobar2.append(int(input('Introduzca el cuarto número: ')))
numeros_a_comprobar2.append(int(input('Introduzca el quinto número: ')))

numeros_a_comprobar2.sort()

print(f'El número más grande es el {numeros_a_comprobar2[-1]}.')


# 8. Diseña un programa que, dado un número real que debe representar la calificación numérica de un examen, proporcione la calificación cualitativa correspondiente al número dado. La calificación cualitativa será una de las siguientes: «Suspenso» (nota menor que 5), «Aprobado» (nota mayor o igual que 5, pero menor que 7), «Notable» (nota mayor o igual que 7, pero menor que 9), «Sobresaliente» (nota mayor o igual que 9, pero menor que 10), «Matrícula de Honor» (nota 10).

calificacion = int(input('Introduzca la calificación: '))

if calificacion < 5:
    print(f'La calificación correspondiente de {calificacion} es suspenso')
elif calificacion < 7:
    print(f'La calificación correspondiente de {calificacion} es aprobado')
elif calificacion < 9:
    print(f'La calificación correspondiente de {calificacion} es notable')
elif calificacion < 9:
    print(f'La calificación correspondiente de {calificacion} es sobresaliente')
else:
    print(f'La calificación correspondiente de {calificacion} es matrícula de honor')

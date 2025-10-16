import math


def main():
    #1. Escribir un programa que pregunte al usuario su nombre, y luego lo salude.

    # nombreUsuario = input('Introduzca su nombre: ')
    # print(f'Hola {nombreUsuario}!')


    # 2. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

    # cateto1 = int(input("Introduzca la longitud del primer cateto: "))
    # cateto2 = int(input("Introduzca la longitud del segundo cateto: "))

    # hipotenusa = math.sqrt(pow(cateto1, 2) + pow(cateto2, 2))

    # print(f'La hipotenusa de un cuadrado rectángulo con un cateto de {cateto1}cm y otro de {cateto2}cm es {hipotenusa}cm')


    # 3. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

    # minutos = int(input("Introduce una cantidad de minutos: "))

    # horas = minutos // 60
    # minutosRestantes = minutos % 60

    # print(f'{minutos} minutos corresponden a {horas} {'horas' if horas > 1 else 'hora'} y {minutosRestantes} {'minutos' if minutosRestantes > 1 else 'minuto'}')


    # 4. Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.

    # numero = input('Introduce un número de dos cifras: ')

    # numeroInvertido = numero[1] + numero[0]

    # print(f'El número inverso de {numero} es {numeroInvertido}')


    # 5. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un programa que determine la hora de llegada a la ciudad B.

    # Pedimos la hora de salida del ciclista
    # horaSalida = int(input('Introduce la hora de salida: '))
    # minutosSalida = int(input('Introduce los minutos de la hora de salida: '))
    # segundosSalida = int(input('Introduce los segundos de la hora de salida: '))

    segundosDeTrayecto = int(input('Introduce los segundos de ruta que tardará el ciclista: '))

    horasDeTrayecto = segundosDeTrayecto // 3600
    restoDeLasHoras = segundosDeTrayecto % 3600
    minutosDeTrayecto = restoDeLasHoras // 60
    segundosDeTrayecto = restoDeLasHoras % 60


    print(f'horas: {horasDeTrayecto} minutos: {minutosDeTrayecto}')



main()
import math


def main():
    
    #1. Escribir un programa que pregunte al usuario su nombre, y luego lo salude.

    nombreUsuario = input('Introduzca su nombre: ')
    print(f'Hola {nombreUsuario}!')


    # 2. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

    cateto1 = int(input("Introduzca la longitud del primer cateto: "))
    cateto2 = int(input("Introduzca la longitud del segundo cateto: "))

    hipotenusa = math.sqrt(pow(cateto1, 2) + pow(cateto2, 2))

    print(f'La hipotenusa de un cuadrado rectángulo con un cateto de {cateto1}cm y otro de {cateto2}cm es {hipotenusa}cm')


    # 3. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

    minutos = int(input("Introduce una cantidad de minutos: "))

    horas = minutos // 60
    minutosRestantes = minutos % 60

    print(f'{minutos} minutos corresponden a {horas} {'horas' if horas > 1 else 'hora'} y {minutosRestantes} {'minutos' if minutosRestantes > 1 else 'minuto'}')


    # 4. Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.

    numero = input('Introduce un número de dos cifras: ')

    numeroInvertido = numero[1] + numero[0]

    print(f'El número inverso de {numero} es {numeroInvertido}')


    # 5. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un programa que determine la hora de llegada a la ciudad B.

    # Pedimos la hora de salida del ciclista
    horaSalida = int(input('Introduce la hora de salida: '))
    minutosSalida = int(input('Introduce los minutos de la hora de salida: '))
    segundosSalida = int(input('Introduce los segundos de la hora de salida: '))

    horaSalidaSegundos = horaSalida * 3600 + minutosSalida * 60 + segundosSalida

    segundosDeTrayecto = int(input('Introduce los segundos de ruta que tardará el ciclista: '))

    horaLlegadaSegundos = horaSalidaSegundos + segundosDeTrayecto

    horasDeTrayecto = horaLlegadaSegundos // 3600
    restoDeLasHoras = horaLlegadaSegundos % 3600
    minutosDeTrayecto = restoDeLasHoras // 60
    horaLlegadaSegundos = restoDeLasHoras % 60

    if segundosDeTrayecto >= 60:
        segundosDeTrayecto = 0
        minutosDeTrayecto += 1
    
    if minutosDeTrayecto >= 60:
        minutosDeTrayecto = 0
        horasDeTrayecto += 1
    
    if horasDeTrayecto >= 24:
        horasDeTrayecto = 0

    print(f'El ciclista llegará al destino a las {horasDeTrayecto}:{minutosDeTrayecto}:{segundosDeTrayecto}')


#  6. Escribir un programa para calcular la nota final de un examen, considerando que:

    # Cada respuesta correcta suma 5 puntos.
    # Cada respuesta incorrecta suma -1 puntos.
    # Cada respuesta en blanco suma 0 puntos. 
    # Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.

    PUNTOS_RESPUESTA_CORRECTA = 5
    PUNTOS_RESPUESTA_INCORRECTA = -1
    PUNTOS_RESPUESTA_BLANCO = 0

    preguntasAcertadas = int(input('Introduce el número de respuestas acertadas: '))
    preguntasFalladas = int(input('Introduce el número de respuestas falladas: '))
    preguntasEnBlanco = int(input('Introduce el número de respuestas en blanco: '))

    preguntasTotales = preguntasAcertadas + preguntasFalladas + preguntasEnBlanco

    puntuacionAlumno = (preguntasAcertadas * PUNTOS_RESPUESTA_CORRECTA) + (preguntasFalladas * PUNTOS_RESPUESTA_INCORRECTA) + (preguntasEnBlanco * PUNTOS_RESPUESTA_BLANCO)

    notaAlumno = (puntuacionAlumno * 10) / (preguntasTotales * PUNTOS_RESPUESTA_CORRECTA)

    print(f'La nota del alumno con {preguntasAcertadas} preguntas acertadas, {preguntasFalladas} preguntas falladas y {preguntasEnBlanco} preguntas en blanco es de: {notaAlumno}')

# ¿Qué tendrías que hacer para facilitar que los puntos que suman los diferentes tipos de respuestas puedan cambiar en el futuro?

#? Habría que cambiar los valores de las constantes para ajustar las puntuaciones de cada tipo de pregunta

main()
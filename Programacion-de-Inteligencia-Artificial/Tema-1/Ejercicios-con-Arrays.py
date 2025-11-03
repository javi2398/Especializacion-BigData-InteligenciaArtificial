import random
import numpy as np

def main():
# 1. Define tres listas de 20 números enteros cada uno, con nombres number, square y cube. Carga las lista number con valores aleatorios entre 0 y 100. En la lista square se deben almacenar los cuadrados de los valores que hay en number. En la lista cube se deben almacenar los cubos de los valores que hay en number. A continuación, muestra el contenido de las tres listas dispuesto en tres columnas.

    # number = []
    # square = []
    # cube = []

    # for _ in range(20):
    #     number.append(random.randint(1, 100))
    
    # for valor in number:
    #     square.append(valor ** 2)
    
    # for valor in number:
    #     cube.append(valor ** 3)

    # for indice in range(len(number)):
    #     print(f'| {number[indice]} | {square[indice]} | {cube[indice]} |')


# 2. Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.


    # number_numpy = np.random.randint(0, 101, 20) # Crea un array con valores enteros aleatorios
    # square_numpy = np.square(number_numpy)
    # cube_numpy = np.power(number_numpy, 3)

    # print(number_numpy)
    # print(square_numpy)
    # print(cube_numpy)

    # for indice in range(len(number_numpy)):
    #     print(f'| {number_numpy[indice]} | {square_numpy[indice]} | {cube_numpy[indice]} |')


# 3. Escribe un programa que genere 20 números enteros aleatorios entre 0 y 100 y que los almacene en un array de numpy. El programa debe ser capaz de pasar todos los números pares a las primeras posiciones del array (del 0 en adelante) y todos los números impares a las celdas restantes. Utiliza arrays auxiliares si es necesario.


    # array_pares_impares = np.random.randint(0, 101, 20)

    # array_pares = array_pares_impares[array_pares_impares % 2 == 0]
    # array_impares = array_pares_impares[array_pares_impares % 2 != 0]

    # array_pares_impares = np.concatenate([array_pares, array_impares])


    # print(array_pares_impares)


# 4. Escribe un programa que lea 5 números por teclado y que los almacene en una lista. Rota los elementos de esa lista, es decir, el elemento de la posición 0 debe pasar a la posición 1, el de la 1 a la 2, etc. El número que se encuentra en la última posición debe pasar a la posición 0. Finalmente, muestra el contenido de la lista.

    # array_valores_usuario = np.array([])

    # for valor in range(5):
    #     numero = int(input(f'Introduce el valor {valor}: '))
    #     array_valores_usuario = np.append(array_valores_usuario, numero)

    # print(array_valores_usuario)

    # # El segundo parámetro indica cuantos lugares queremos moverlo, si es negativo los rota a la izquierda
    # array_valores_usuario = np.roll(array_valores_usuario, 1)

    # print(array_valores_usuario)


# 5. Escribe un programa que genere 20 números enteros entre 100 y 999. Estos números se deben introducir en una lista de 4 filas por 5 columnas. El programa mostrará las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara. La suma total debe aparecer en la esquina inferior derecha.

    array_valores = [[] for _ in range(4)]
    acumulador_fila = 0
    acumulador_total = 0

    for fila in range(4):
        for columna in range(5):
            array_valores[fila].append(random.randint(100, 999))
            acumulador_fila = acumulador_fila + array_valores[fila][columna]
            acumulador_total = acumulador_total + array_valores[fila][columna]

        # Añadimos la suma de la fila al final
        array_valores[fila].append(acumulador_fila)
        acumulador_fila = 0
    # Añadimos la suma total al final de la ultima fila
    array_valores[-1].append(acumulador_total)


    # print(array_valores)

# 6. Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.

    array_valores_numpy = np.random.randint(100, 999, (4, 5))

    suma_total = array_valores_numpy.sum()

    # Añadir columna de sumas de filas
    array_valores_numpy = np.hstack((array_valores_numpy, array_valores_numpy.sum(axis=1).reshape(-1, 1)))

    print(array_valores_numpy, suma_total)


if __name__ == "__main__":
    main()
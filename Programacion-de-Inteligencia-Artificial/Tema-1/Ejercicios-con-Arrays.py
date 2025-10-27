import random

def main():
# 1. Define tres listas de 20 números enteros cada uno, con nombres number, square y cube. Carga las lista number con valores aleatorios entre 0 y 100. En la lista square se deben almacenar los cuadrados de los valores que hay en number. En la lista cube se deben almacenar los cubos de los valores que hay en number. A continuación, muestra el contenido de las tres listas dispuesto en tres columnas.

    number = []
    square = []
    cube = []

    for _ in range(20):
        number.append(random.randint(1, 100))
    
    for valor in number:
        square.append(valor ** 2)
    
    for valor in number:
        cube.append(valor ** 3)

    for indice in range(len(number)):
        print(f'| {number[indice]} | {square[indice]} | {cube[indice]} |')


# 2. Haz el ejercicio anterior usando numpy y aprovechando sus ventajas.

    import numpy

    



if __name__ == "__main__":
    main()
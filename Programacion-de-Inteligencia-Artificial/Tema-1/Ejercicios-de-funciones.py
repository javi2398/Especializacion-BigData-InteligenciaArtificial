def main():

    # Ejercicio 1

    # Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: sumar, restar, multiplicar, dividir y terminar. Cada opción llama a una función a la que se le pasan las dos variables y muestra el resultado de la operación. Si se introduce una opción incorrecta se muestra un mensaje de error. El menú se volverá a mostrar, a menos que no se de a la opción terminar.
    # Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera). Las variables se inicializan a cero.
    # Modifica el programa anterior para que si no se introducen las dos variables desde la opción correspondiente no se puedan ejecutar el resto de las opciones.
    # Crea una función para gestionar menús: recibe una lista de opciones, las muestra numeradas, pide una opción (por su número) y devuelve la opción escogida. Modifica el último programa para que use esta función. 

    # primer_valor = 0
    # segundo_valor = 0
    # valor_menu = 100
    # variables_definidas = False

    # def gestion_menu():
    #     opciones_introducidas = []
    #     opcion = 1

    #     while opcion != '0':
    #         opcion = input('Introduce las opciones deseadas o pulse 0 para salir: ')

    #         if opcion != '0':
    #             opciones_introducidas.append(opcion)
    #             print(f'{opcion} guardada')

    #     if opciones_introducidas:
    #         print('Pulse 0 para salir')

    #         for opciones in range(1, len(opciones_introducidas)):
    #             print(f'Pulse {opciones} para {opciones_introducidas[opciones - 1]}')
                
    #         seleccion = int(input('Seleccione la opción deseada: '))

    #         if seleccion == 0:
    #             print('Ha salido del menú.')
    #         else:
    #             print(f'Ha elegido la opción {seleccion}: {opciones_introducidas[seleccion - 1]}')

    #     print('Ha salido de la gestión de menú')


    # while valor_menu != 0:

    #     try:
    #         valor_menu = int(input('Seleccione la opción deseada: \n 1 Introducir variables \n 2 SUMAR \n 3 RESTAR \n 4 MULTIPLICAR \n 5 DIVIDIR \n 6 PERSONALIZAR MENU \n o pulse 0 para salir. \n'))
    #     except ValueError:
    #         print('El valor ingresado no es número válido.')

    #     if valor_menu == 1 and not variables_definidas:
    #         try:
    #             primer_valor = int(input('Introduce el primer valor: '))
    #             segundo_valor = int(input('Introduce el segundo valor: '))
    #             variables_definidas = True
    #         except ValueError:
    #             print('El valor ingresado no es número válido.')
    #     elif not variables_definidas:
    #         print('Debe introducir las variables primero.')

    #     if valor_menu != 0 and variables_definidas:
    #         match valor_menu:
    #             case 1:
    #                 pass
    #             case 2:
    #                 print('El resultado de la suma es: ', primer_valor + segundo_valor)
    #             case 3:
    #                 print('El resultado de la resta es: ', primer_valor - segundo_valor)
    #             case 4:
    #                 print('El resultado de la multiplicación es: ', primer_valor * segundo_valor)
    #             case 5:
    #                 print('El resultado de la división es: ', primer_valor / segundo_valor)
    #             case 6:
    #                 gestion_menu()
    #             case _:
    #                 print('Ha introducido un valor no definido')

    # print('Ha salido del programa.')



    # Crea una biblioteca de funciones numéricas que contenga las siguientes funciones. Recuerda que puedes usar unas dentro de otras si es necesario.

    # Observa bien lo que hace cada función ya que, si las implementas en el orden adecuado, te puedes ahorrar mucho trabajo. Por ejemplo, la función is_palindromic() resulta trivial teniendo reverse() y la función next_prime() también es muy fácil de implementar teniendo is_prime().

    # Está prohibido usar funciones de conversión del número a una cadena.

    # is_palindromic: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.
    # is_prime: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.
    # next_prime: devuelve el menor primo que es mayor al número que se pasa como parámetro.
    # digits: devuelve el número de dígitos de un número entero. ------
    # reverse: le da la vuelta a un número.
    # digit_n: devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de izquierda a derecha.
    # digit_position: da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se encuentra, devuelve -1.
    # remove_behind: le quita a un número n dígitos por detrás (por la derecha). -------------------------
    # remove_ahead: le quita a un número n dígitos por delante (por la izquierda).
    # paste_behind: añade un dígito a un número por detrás. -----------------
    # paste_ahead: añade un dígito a un número por delante. --------------------
    # piece_of_number: toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo correspondiente.
    # concatenate: pega dos números para formar uno. ---------------------
    # Haz el programa de manera que al ejecutarse pruebe cada una de las funciones.

    def digits(numero):
        contador_digitos = 1
        comparador = 9

        while numero > comparador:
            contador_digitos += 1
            comparador = comparador * 10 + 9
        
        print(f'El valor {numero} contiene {contador_digitos} digitos.')
        return contador_digitos


    def remove_behind(numero, digitos_a_remover):

        print(f'El valor {numero} al removerle {digitos_a_remover} digitos, corresponde a: {numero // (10 ** digitos_a_remover)}.')
        return numero // (10 ** digitos_a_remover)


    def paste_behind(numero, digitos_a_anadir):

        print(f'El valor {numero} al añadirle el dígito {digitos_a_anadir}, corresponde a: {numero * 10 + digitos_a_anadir}.')
        return(numero * 10 + digitos_a_anadir)


    def remove_ahead(numero, digitos_a_remover):
        total_digitos = digits(numero)

        if digitos_a_remover >= total_digitos:
            print(f'El valor {numero} al removerle {digitos_a_remover} dígitos, corresponde a: 0.')
            return 0
        else:
            numero_removido = numero % (10 ** (total_digitos - digitos_a_remover))
            print(f'El valor {numero} al removerle {digitos_a_remover} dígitos, corresponde a: {numero_removido}.')
            return numero_removido

    def paste_ahead(numero, numero_a_anadir):

        total_digitos = digits(numero)
        print(f'El valor {numero} al añadirle el valor {numero_a_anadir} delante, corresponde a: {numero_a_anadir * (10 ** total_digitos) + numero}.')

        return numero_a_anadir * (10 ** total_digitos) + numero


    def concatenate(numero1, numero2):

        print(f'Al juntar el número {numero1} y el número {numero2} nos da como resultado {numero1 * (10 ** digits(numero2)) + numero2}.')
        return numero1 * (10 ** digits(numero2)) + numero2


    def reverse(numero_a_voltear):

        if numero_a_voltear <= 9:
            print(f'El valor {numero_a_voltear} no se puede voltear.')
            return numero_a_voltear

        numero_reverso = 0

        while numero_a_voltear > 0: 
            numero_reverso = numero_reverso * 10 + (numero_a_voltear % 10); 
            numero_a_voltear //= 10
        
        print(f'El valor {numero_a_voltear} volteado corresponde a {numero_reverso}')
        return numero_reverso


    def digit_n(numero, indice):
        total = digits(numero)
        if indice < 0 or indice >= total:
            print(f'El índice {indice} está fuera del rango del número {numero}.')
            return -1
        numero_reducido = remove_behind(numero, total - indice - 1)
        resultado = numero_reducido % 10
        print(f'El dígito en la posición {indice} del número {numero} es {resultado}.')
        return resultado


    def digit_position(numero, digito):
        total = digits(numero)
        for i in range(total):
            if digit_n(numero, i) == digito:
                print(f'El dígito {digito} se encuentra por primera vez en la posición {i} del número {numero}.')
                return i
        print(f'El dígito {digito} no se encuentra en el número {numero}.')
        return -1


    def piece_of_number(numero, inicio, fin):
        total = digits(numero)
        if inicio < 0 or fin >= total or inicio > fin:
            print(f'Error: las posiciones {inicio} a {fin} no son válidas para el número {numero}.')
            return -1
        temp = remove_ahead(numero, inicio)
        longitud = fin - inicio + 1
        resultado = remove_behind(temp, digits(temp) - longitud)
        print(f'El trozo del número {numero} entre las posiciones {inicio} y {fin} es {resultado}.')
        return resultado


    def is_prime(numero):
        if numero < 2:
            print(f'El número {numero} no es primo.')
            return False
        if numero == 2 or numero == 3:
            print(f'El número {numero} es primo.')
            return True
        if numero % 2 == 0 or numero % 3 == 0:
            print(f'El número {numero} no es primo.')
            return False
        i = 5
        while i * i <= numero:
            if numero % i == 0 or numero % (i + 2) == 0:
                print(f'El número {numero} no es primo.')
                return False
            i += 6
        print(f'El número {numero} es primo.')
        return True


    def next_prime(numero):
        candidato = numero + 1
        while not is_prime(candidato):
            candidato += 1
        print(f'El siguiente número primo después de {numero} es {candidato}.')
        return candidato


    def is_palindromic(numero):
        if numero == reverse(numero):
            print(f'El número {numero} es capicúa.')
            return True
        else:
            print(f'El número {numero} no es capicúa.')
            return False


    digits(999)
    remove_behind(999, 2)
    paste_behind(99, 8)
    remove_ahead(999, 2)
    paste_ahead(999, 2)
    concatenate(20, 34)
    reverse(21)
    digit_n(98765, 2)
    digit_position(98765, 7)
    piece_of_number(123456, 1, 3)
    is_prime(29)
    next_prime(29)
    is_palindromic(12321)


if __name__ == "__main__":
    main()
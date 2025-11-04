# 1. Crea una clase, y pruébala, que modele fracciones. Debe permitir:

# Crear fracciones indicando numerador y denominador.
#  Ejemplo: f = Fraction(2, 3)
# Ojo!!! No se puede tener un denominador cero.
# Las fracciones pueden operar entre sí.
# Sumar, multiplicar, dividir, restar.
# Ojo!!! esto se puede hacer: f + 1, 5 * f
# Las fracciones se pueden comparar.
# ==, <, <=, >, >=, !=
# Ojo!!! estas dos fracciones son iguales: 1/2 y 2/4
# Ojo!!! esto se puede hacer 1 < 1/2

import math

class Fraction:

    def __init__(self, numerador, denominador):
        if denominador > 0:
            self.__numerador = numerador
            self.__denominador = denominador
            self._simplificar()


    def __str__(self):
        return str(f'{self.__numerador:02d}/{self.__denominador:02d}')
    
    def _simplificar(self):
        maximo_comun_divisor = math.gcd(self.__numerador, self.__denominador)
        self.__numerador = self.__numerador // maximo_comun_divisor
        self.__denominador = self.__denominador // maximo_comun_divisor

    def _calcular_valor(self):
        if isinstance(self, Fraction):
            return self.__numerador / self.__denominador
        else:
            return self
    
    def _conversor_fraccion(self, other):
        if isinstance(other, Fraction):
            return other
        else:
            return Fraction(other, 1)
    
    def __add__(self, other):
        other = self._conversor_fraccion(other)
        return Fraction(numerador=(self.__numerador * other.__denominador + self.__denominador * other.__numerador), denominador=(self.__denominador * other.__denominador))

    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        other = self._conversor_fraccion(other)
        return Fraction(numerador=(self.__numerador * other.__denominador - self.__denominador * other.__numerador), denominador=(self.__denominador * other.__denominador))
    
    def __rsub__(self, other):
        other = self._conversor_fraccion(other)
        return other - self
    
    def __mul__(self, other):
        other = self._conversor_fraccion(other)
        return Fraction(numerador=(self.__numerador * other.__denominador), denominador=(self.__denominador * other.__denominador))
    
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __rtruediv__(self, other):
        other = self._conversor_fraccion(other)
        return other / self

    def __truediv__(self, other):
        other = self._conversor_fraccion(other)
        return Fraction(numerador=(self.__numerador * other.__denominador), denominador=(self.__denominador * other.__numerador))

    def __gt__(self, other):
        other = self._conversor_fraccion(other)
        return self._calcular_valor() > other._calcular_valor()
    
    def __ge__(self, other):
        other = self._conversor_fraccion(other)
        return self._calcular_valor() >= other._calcular_valor()
    
    def __lt__(self, other):
        other = self._conversor_fraccion(other)
        return self._calcular_valor() < other._calcular_valor()
    
    def __le__(self, other):
        other = self._conversor_fraccion(other)
        return self._calcular_valor() <= other._calcular_valor()
    
    def __eq__(self, other):
        other = self._conversor_fraccion(other)
        return self._calcular_valor() == other._calcular_valor()
    
    def __ne__(self, other):
        other = self._conversor_fraccion(other)
        return self._calcular_valor() != other._calcular_valor()




def main():

    f1 = Fraction(1, 2)
    f2 = Fraction(2, 4)
    f3 = Fraction(3, 4)
    f4 = Fraction(5, 3)

    print("Primera fracción:", f1)
    print("Segunda fracción:", f2)
    print("Tercera fracción:", f3)
    print("Cuarta fracción:", f4)
    print()

    # Probar suma
    suma = f1 + f3
    print("Suma (+):", suma)

    # Probar resta
    resta = f3 - f1
    print("Resta (-):", resta)

    # Probar multiplicación
    producto = f1 * f3
    print("Multiplicación (*):", producto)

    # Probar división
    division = f4 / f1
    print("División (/):", division)
    print()

    # Operaciones con enteros
    print("Suma con entero (f1 + 1):", f1 + 1)
    print("Multiplicación con entero (5 * f1):", 5 * f1)
    print("División entre entero (f1 / 2):", f1 / 2)
    print("Resta desde entero (1 - f1):", 1 - f1)
    print()

    # Comparaciones entre fracciones
    print("¿f1 == f2?", f1 == f2)
    print("¿f1 != f3?", f1 != f3)
    print("¿f1 < f3?", f1 < f3)
    print("¿f3 > f1?", f3 > f1)
    print("¿f3 <= f4?", f3 <= f4)
    print("¿f4 >= f1?", f4 >= f1)
    print()

    # Comparaciones con enteros
    print("¿1 < f1?", 1 < f1)
    print("¿f1 < 1?", f1 < 1)

    # Fracciones equivalentes
    print("¿1/2 y 2/4 son iguales?", f1 == f2)


if __name__ == "__main__":
    main()
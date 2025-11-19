# 3. En Python podemos manejar fechas pero no nos gusta, vamos a crear una clase Date. Debe permitir:

# Crear fechas.
# Ejemplo: f = Date(17, 11, 2022)
# Ojo!!! Estas fechas son erróneas: 
# Date(78, -45, 0)
# Date(31, 6, 2022)
# Date(29, 2, 2022)
# Las fechas se pueden comparar.
# A las fechas se le pueden sumar y restar días.
# Las fechas se pueden restar.
# Se debe poder averiguar el día de la semana de una fecha.

from typeguard import typechecked

@typechecked
class Date: 

    def __init__(self, day: int = 1, month: int = 1, year: int = 1):

        if not (1 <= month <= 12):
            raise ValueError("El mes debe estar entre 1 y 12")
        if not (1 <= day <= 31):
            raise ValueError("El día debe estar entre 1 y 31")
        if year < 1:
            raise ValueError("El año debe ser positivo")
        
        self.__day = day
        self.__month = month
        self.__year = year
        print(self._conversor_fecha())


    def __str__(self):
        return str(f'{self.__day:02d}/{self.__month:02d}/{self.__year:04d}')
    
    # Devuelvo la fecha en formato YYYYMMDD para poder comparar
    def _conversor_fecha(self):
        return int(f'{self.__year}{self.__month:02d}{self.__day:02d}')
    
    def add_days(self, days_to_add: int):
        self.__day += days_to_add

        if self.__month == 2 and self.__day > 28:
            self.__month += self.__day // 28
            self.__day %= 28
        # Los meses pares tienen 30 dias excepto Febrero
        elif self.__month % 2 == 0 and self.__day > 30:
            self.__month += self.__day // 30
            self.__day %= 30
        elif self.__month % 2 != 0 and self.__day > 31:
            self.__month += self.__day // 31
            self.__day %= 31
        
        if self.__month > 12:
            self.__year = self.__year + self.__month // 12
    
    # Método de Tomohiko Sakamoto
    def day_of_week(self):
        day = self.__day
        month = self.__month
        year = self.__year

        t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        if month < 3:
            year -= 1
        weekday = (year + year//4 - year//100 + year//400 + t[month-1] + day) % 7
        days = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
        return days[weekday]

    
    # def __add__(self, other):
    #     other = self._conversor_fraccion(other)
    #     return Fraction(numerador=(self.__numerador * other.__denominador + self.__denominador * other.__numerador), denominador=(self.__denominador * other.__denominador))

    # def __radd__(self, other):
    #     return self.__add__(other)
    
    # def __sub__(self, other):
    #     other = self._conversor_fraccion(other)
    #     return Fraction(numerador=(self.__numerador * other.__denominador - self.__denominador * other.__numerador), denominador=(self.__denominador * other.__denominador))
    
    # def __rsub__(self, other):
    #     other = self._conversor_fraccion(other)
    #     return other - self

    def __gt__(self, other):
        return self._conversor_fecha() > other._conversor_fecha()
    
    def __ge__(self, other):
        return self._conversor_fecha() >= other._conversor_fecha()
    
    def __lt__(self, other):
        return self._conversor_fecha() < other._conversor_fecha()
    
    def __le__(self, other):
        return self._conversor_fecha() <= other._conversor_fecha()
    
    def __eq__(self, other):
        return self._conversor_fecha() == other._conversor_fecha()
    
    def __ne__(self, other):
        return self._conversor_fecha() != other._conversor_fecha()




def main():

    f1 = Date(1, 2, 2020)
    # f2 = Fraction(2, 4)
    # f3 = Fraction(3, 4)
    # f4 = Fraction(5, 3)


if __name__ == "__main__":
    main()
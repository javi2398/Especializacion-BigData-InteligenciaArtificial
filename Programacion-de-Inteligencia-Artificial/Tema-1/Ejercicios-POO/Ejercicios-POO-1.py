# 1. En Python existen clases para manipular duraciones de tiempo (horas:minutos:segundos), pero no nos gustan, vamos a hacer una nueva que se llamará Duration y será inmutable. Debe permitir:

# Crear duraciones de tiempos.
# Ejemplo: t = Duration(10,20,56)
# Ojo!!! (10, 62, 15) se debe guardar como (11, 2, 15)
# Si no indico la hora, minuto o segundo estos valores son cero:
# Duration() --> (0, 0, 0)
# Duration(34) --> (34, 0, 0)
# Duration(34, 15) --> (34, 15, 0)
# Duration(34, 61) --> (35, 1, 0)
# Las duraciones de tiempo se pueden comparar.
# A las duraciones de tiempo les puedo sumar y restar segundos.
# Las duraciones de tiempo se pueden sumar y restar.

class Duration:

    def __init__(self, horas=0, minutos=0, segundos=0):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos
        self._ajustar_horas()

    # :02d significa: 0 → rellenar con ceros, 2 → el ancho total debe ser de 2 caracteres, d → es un número entero (“decimal”)
    def __str__(self):
        return str(f'{self.__horas:02d}:{self.__minutos:02d}:{self.__segundos:02d}')
    
    def __add__(self, other):
        return Duration(self.__horas + other.__horas, self.__minutos + other.__minutos, self.__segundos + other.__segundos)
    
    def __sub__(self, other):
        nueva_hora_segundos = self._total_segundos() - other._total_segundos()
        return Duration(segundos=abs(nueva_hora_segundos))

    def __gt__(self, other):
        return self._total_segundos() > other._total_segundos()
    
    def __ge__(self, other):
        return self._total_segundos() >= other._total_segundos()
    
    def __lt__(self, other):
        return self._total_segundos() < other._total_segundos()
    
    def __le__(self, other):
        return self._total_segundos() <= other._total_segundos()
    
    def __eq__(self, other):
        return self._total_segundos() == other._total_segundos()

    def anadir_segundos(self, segundos_a_anadir):
        self.__segundos += segundos_a_anadir
        self._ajustar_horas()

    def _ajustar_horas(self):
        minutos_sobrantes = self.__segundos // 60

        if minutos_sobrantes:
            self.__segundos = self.__segundos % 60
            self.__minutos += minutos_sobrantes

        if self.__minutos > 59:
            horas_sobrantes = self.__minutos // 60
            self.__minutos = self.__minutos % 60
            self.__horas += horas_sobrantes
        
        if self.__horas > 23:
            self.__horas = self.__horas % 24

    def _total_segundos(self):
        return self.__horas * 3600 + self.__minutos * 60 + self.__segundos



def main():
    primeraHora = Duration(23, 65, 65) 
    segundaHora = Duration(10, 10, 10)

    print("Primera hora:", primeraHora)
    print("Segunda hora:", segundaHora)

    # Probar suma
    terceraHora = primeraHora + segundaHora
    print("Suma (+):", terceraHora)

    # Probar resta
    cuartaHora = primeraHora - segundaHora
    print("Resta (-):", cuartaHora)

    # Añadir segundos manualmente
    primeraHora.anadir_segundos(3600)
    print("Después de añadir 3600 segundos a la primera hora:", primeraHora)

    # Comparaciones
    print("¿primeraHora > segundaHora?", primeraHora > segundaHora)
    print("¿primeraHora >= segundaHora?", primeraHora >= segundaHora)
    print("¿primeraHora < segundaHora?", primeraHora < segundaHora)
    print("¿primeraHora <= segundaHora?", primeraHora <= segundaHora)
    print("¿primeraHora == segundaHora?", primeraHora == segundaHora)
    print("¿primeraHora != segundaHora?", primeraHora != segundaHora)


if __name__ == "__main__":
    main()
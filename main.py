from clases.Palindromo import *
from clases import Palindromos_Instancias
from clases.Logger import *
import time


def seleccionejercicio(variable):
    if variable == 1:
        p = Palindromo
        print(p.esPalindromo(str(input(
            "Introduzca una frase/palabra/número para comprobar si es palíndromo: "))))
    elif variable == 2:
        palabra = str(
            input("Introduzca una frase/palabra/número para comprobar si es palíndromo: "))
        Palindromos_Instancias.Palindromos(palabra).ejecutar()
    elif variable == 3:
        print("En desarrollo...")
    elif variable == 4:
        l = Logger
        print(l.seguimientollamadas(input(
            "Introduzca la cantidad de llamadas que usted desea incluir en el registro: ")))

    else:
        print("Introduzca valores correctos por favor.")
        seleccionejercicio(int(input("""
1 - Palíndromo(Método de clase).
2 - Palíndromo(Método de instancia).
3 - Puzzle.
4 - Logger.

Seleccione que ejercicio desea ejecutar(1-4): """)))


variable = int(input("""
1 - Palíndromo(Método de clase).
2 - Palíndromo(Método de instancia).
3 - Puzzle.
4 - Logger.

Seleccione que ejercicio desea ejecutar(1-4): """))

if __name__ == "__main__":
    seleccionejercicio(variable)
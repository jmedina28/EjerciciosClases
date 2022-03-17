from clases.Palindromo import *
def seleccionejercicio(variable):

    if variable == 1:
        p = Palindromo
        print(p.esPalindromo(str(input(
            "Introduzca una frase/palabra/número para comprobar si es palíndromo: "))))
    elif variable == 2:
        print("En desarrollo...")
    elif variable == 3:
        print("En desarrollo...")
    elif variable == 4:
        print("En desarrollo...")
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

seleccionejercicio(variable)
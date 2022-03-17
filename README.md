<h1 align="center">Clases</h1>

<h3 align="center">Autores de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)
1. [@xavitheforce](https://github.com/Xavitheforce)
---
En este [repositorio](https://github.com/jmedina28/EjerciciosClases) quedan resueltos los ejercicios de clases para POO. Para llevar a cabo el proyecto nos hemos documentado a través de la teoría que se encuentra en el campus virtual y de diversas fuentes que hemos encontrado.
***
## Índice
1. [Palíndromo (Método de clase).](#id1)
3. [Palíndromo (Método de instancia).](#id2)
3. [Puzzle.](#id3)
4. [Logger.](#id4)
***

## Ejercicio 1: Palíndromo (Método de clase)<a name="id1"></a>

En este ejercicio he creado la clase Palindromo la cual contiene el método esPalindromo() el cual comprueba si una frase, una palabra, una combinación numérica o de símbolos forman palíndromos.

El código empleado para resolverlo es el siguiente:

```python
# Palíndromos

class Palindromo:

    def esPalindromo(contenido):
        a, b = 'áéíóúüñÁÉÍÓÚÜ', 'aeiouunAEIOUU'
        tilde = str.maketrans(a, b)
        contenido = contenido.lower()  # Convierto el texto en minúsculas.
        contenido = contenido.replace(' ', '')  # Quito los espacios.
        contenido = contenido.translate(tilde)  # Elimino las tildes.
        lista = list(contenido)  # Convierto el contenido en una lista.
        listaresultado = list(reversed(contenido))  # Invierto la lista.
        if lista == listaresultado:  # Comparo el contenido original con el inverso.
            print(True)
            exit()
        else:
            print(False)
            exit()
```
El UML es el siguiente:



## Ejercicio 2: Palíndromo (Método de instancia)<a name="id2"></a>

En este ejercicio...


El código empleado para resolverlo es el siguiente:
 
 ```python
# Palíndromos

from operator import truediv
import os
import re


class Palindromos():
    def __init__(self, atributo):
        self.atributo = atributo

    def test(self, contenido):
        a, b = 'áéíóúüñÁÉÍÓÚÜ', 'aeiouunAEIOUU'
        self.tilde = str.maketrans(a, b)
        contenido = contenido.lower()  # Convierto el texto en minúsculas.
        contenido = contenido.replace(' ', '')  # Quito los espacios.
        contenido = contenido.translate(self.tilde)  # Elimino las tildes.
        self.lista = list(contenido)  # Convierto el atributo en una lista.
        # Invierto la lista.
        self.listaresultado = list(reversed(contenido))
        # Comparo el atributo original con el inverso.
        if self.lista == self.listaresultado:
            return True
        else:
            return False

    def destructor(self):
        self.doct = open("Palindromos.txt", "r")
        ultima_linea = self.doct.readlines()[-1]
        if Palindromos(self.atributo).test(self.atributo) == False:
            print(str(ultima_linea))
        self.doct.close()

    def ejecutar(self):
        self.doct = open("Palindromos.txt", "r")
        self.ultima_linea = self.doct.readlines()[-1]
        if self.ultima_linea != "#" and Palindromos(self.atributo).test(self.ultima_linea) == True:
            print(str(self.ultima_linea))
        self.doct.close()
        self.m_atributo = Palindromos(self.atributo).atributo.upper()
        self.doct = open("Palindromos.txt", "a")
        self.doct.write("\n"+str(self.m_atributo))
        self.doct.close()
        if Palindromos(self.atributo).test(self.atributo) == True:
            print(True)
        else:
            print(False)
        Palindromos(self.atributo).destructor()
```

El UML es el siguiente:


## Ejercicio 3: Puzzle<a name="id3"></a>

En este ejercicio...


El código empleado para resolverlo es el siguiente:
 
 ```python

```
El UML es el siguiente:

## Ejercicio 4: Logger<a name="id4"></a>

En este ejercicio...


El código empleado para resolverlo es el siguiente:
 
 ```python

```
El UML es el siguiente:


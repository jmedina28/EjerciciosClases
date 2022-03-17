# Palíndromos
from operator import truediv
import os

class Palindromos():
    def __init__(self, atributo):
        self.atributo = atributo

    def test(self, contenido):
            self.doct = open("Palindromos.txt", "w")
            ultima_linea = self.doct.readlines()[-1]
            if Palindromos().test(str(ultima_linea)) == True:
                print(str(ultima_linea))
            self.mayuscula = contenido.upper()
            self.doct.write(str(self.mayuscula)+os.linesep)
            self.doct.close()
            a, b = 'áéíóúüñÁÉÍÓÚÜ', 'aeiouunAEIOUU'
            self.tilde = str.maketrans(a, b)
            contenido = contenido.lower()  # Convierto el texto en minúsculas.
            contenido = contenido.replace(' ', '')  # Quito los espacios.
            contenido = contenido.translate(self.tilde)  # Elimino las tildes.
            self.lista = list(contenido)  # Convierto el atributo en una lista.
            self.listaresultado = list(reversed(contenido))  # Invierto la lista.
            if self.lista == self.listaresultado:  # Comparo el atributo original con el inverso.
                print(True)
                return True
            else:
                print(False)
                return False

    def destructor(self):
        self.doct = open("Palindromos.txt", "r")
        ultima_linea = self.doct.readlines()[-1]
        if Palindromos().test(self.atributo) == False:
            print(str(ultima_linea))
        self.doct.close()


    def ejecutar(self):
        Palindromos().test(self.atributo)
        Palindromos().destructor()
# Palíndromos
from operator import truediv
import os
import re

class Palindromos():
    def __init__(self, atributo):
        self.atributo = atributo
        self.m_atributo = self.atributo.upper()
        self.doct = open("Palindromos.txt", "w")
        self.doct.write(str(self.m_atributo)+os.linesep)
        self.doct.close()

    def test(self, contenido):
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
        if Palindromos(self.atributo).test(self.atributo) == False:
            print(str(ultima_linea))
        self.doct.close()

    def ejecutar(self):
        self.doct = open("Palindromos.txt", "r")
        ultima_linea = self.doct.readlines()[-1]
        if Palindromos(self.atributo).test(self.atributo) == True:
            print(str(ultima_linea))
        self.doct.close()
        Palindromos(self.atributo)
        Palindromos(self.atributo).test(self.atributo)
        Palindromos(self.atributo).destructor()


Palindromos("ana").ejecutar()
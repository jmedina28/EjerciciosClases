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
            self.listaresultado = list(reversed(contenido))  # Invierto la lista.
            if self.lista == self.listaresultado:  # Comparo el atributo original con el inverso.
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
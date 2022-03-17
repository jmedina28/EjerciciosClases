# Palíndromos
import os

class Palindromo:
    def __init__(self, atributo):
        self.atributo = atributo
        self.doct = open("Palindromos.txt", "w")

    def test(self):
            self.doct.write(str(self.atributo)+os.linesep)
            a, b = 'áéíóúüñÁÉÍÓÚÜ', 'aeiouunAEIOUU'
            tilde = str.maketrans(a, b)
            self.atributo = self.atributo.lower()  # Convierto el texto en minúsculas.
            self.atributo = self.atributo.replace(' ', '')  # Quito los espacios.
            self.atributo = self.atributo.translate(tilde)  # Elimino las tildes.
            self.lista = list(self.atributo)  # Convierto el atributo en una lista.
            self.listaresultado = list(reversed(self.atributo))  # Invierto la lista.
            if self.lista == self.listaresultado:  # Comparo el atributo original con el inverso.
                print(True)
            else:
                print(False)
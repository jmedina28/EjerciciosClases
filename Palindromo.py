# Palíndromos
class Palindromo():
    def palindromo(contenido):
        a, b = 'áéíóúüñÁÉÍÓÚÜ', 'aeiouunAEIOUU'
        tilde = str.maketrans(a, b)
        contenido = contenido.lower()  # Convierto el texto en minúsculas.
        contenido = contenido.replace(' ', '')  # Quito los espacios.
        contenido = contenido.translate(tilde)  # Elimino las tildes.
        lista = list(contenido)  # Convierto en el contenido en una lista.
        listaresultado = list(reversed(contenido))  # Invierto la lista.
        if lista == listaresultado:  # Comparo el contenido original con el inverso.
            print("Esta frase/palabra/número es un palíndromo.")
        else:
            print("No es palíndromo.")
    contenido = str(input("Introduzca una frase/palabra/número: "))
    palindromo(contenido)
# Logger


import os
import time

class Logger:

    def seguimientollamadas(n):
        print("Se está generando el fichero de texto...")
        fichero = open("Logger.txt", "a")
        fichero.write("--Start log--")

        for i in range(1, int(n)+1):
            if i == 1:
                fichero.write("\nPrimera llamada.")
            else:
                fichero.write("\n" + str(i) + " llamada.")
        fichero.write("\n--End log: " + str(n) + " log(s)--")
        fichero.close()
        time.sleep(4)
        print("Usted ya puede abrir el fichero que se encuentra dentro de la carpeta en la que está ejecutando esto.")
        time.sleep(8)
        variable = int(input(
            "¿Desea limpiar el registro? (Pulse 1 en caso afirmativo, en caso contrario pulse cualquier otro valor): "))
        if variable == 1:
            os.remove("Logger.txt")
        else:
            print("En este caso, si desea volver a ejecutar el programa tendrá que eliminar manualmente el fichero de texto.")
            exit()

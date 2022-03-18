class A: 
    def z(self): 
        return self 
 
    def y(self, t): 
        return len(t) 
 
a = A # a es la clase definida A
y = a.z # esta linea crea una variable "y" y la convierte en la funcion z de la clase A
print(y(a)) #La variable y (que es la funcion z de la clase A) recoge un valor y lo devuelve.
#En este caso y recoge a, que es la clase A, y por eso devuelve <class '__main__.A'>
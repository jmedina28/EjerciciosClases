class A: 
    def z(self): 
        return self 
 
    def y(self, t): 
        return len(t)
 
a = A # a es la clase definida A
y = a.z # esta linea crea una variable "y" y la convierte en la funcion z de la clase A
print(y(a)) #La variable y (que es la funcion z de la clase A) recoge un valor y lo devuelve.
#En este caso y recoge a, que es la clase A, y por eso devuelve <class '__main__.A'>
aa = a() #ambos son la misma clase, pero variables distintas
print(a())
print(aa)
print(aa is a()) #El resultado es Falso porque los objetos(las clase) estan "guardadas" en posiciones distintas,
# asi que aunque funcionalmente son lo mismo, la maquina las recuerda/almacena de distinta manera
z = aa.y #Convierte la variable z en la funcion y que devuelve la longuitud de una variable
print(z(())) #la funcion y recibiendo un valor (tupla) vacio, por lo que devuelve 0
print(a().y((a,))) #la funcion y de la clase A recibiendo un valor (tupla) de 1 elemento, por lo que devuelve 1
print(A.y(aa, (a,z)))
print(aa.y((z,1,'z')))
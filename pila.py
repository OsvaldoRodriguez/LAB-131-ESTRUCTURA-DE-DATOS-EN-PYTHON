class Pila:
    def __init__(self):
        self.max = 100
        self.tope = 0
        self.A = [None] * (self.max + 1)

    def esvacia(self):
        return self.tope == 0

    def esllena(self):
        return self.max == self.tope

    def nro_elem(self):
        return self.tope

    def adicionar(self, x):
        if not self.esllena():
            self.tope += 1
            self.A[self.tope] = x
        else:
            print("pila llena")

    def eliminar(self):
        cur = None
        if not self.esvacia():
            cur = self.A[self.tope]
            self.tope -= 1
        else:
            print("pila vacia")
        return cur

    def vaciar(self, p):
        while not p.esvacia():
            self.adicionar(p.eliminar())

    def mostrar(self):
        if self.esvacia():
            print("pila vacia")
        else:
            print("datos de la pila")
            aux = Pila()
            while not self.esvacia():
                cur = self.eliminar()
                cur.mostrar()
                aux.adicionar(cur)
            self.vaciar(aux)

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")


def solucion_a(pila):
    aux = Pila()
    mx = 0 # edad maxima
    while not pila.esvacia():
        cur = pila.eliminar()
        mx = max(mx, cur.edad)
        aux.adicionar(cur)

    while not aux.esvacia():
        cur = aux.eliminar()
        if(mx == cur.edad):
            cur.mostrar()
        pila.adicionar(cur)

def solucion_b(pila, nombre):
    aux = Pila()
    flag = False
    while not pila.esvacia():
        cur = pila.eliminar()
        if cur.nombre == nombre:
            flag = True
        aux.adicionar(cur)
    pila.vaciar(aux)
    if flag == True:
        print('si existe')
    else:
        print("no existe")

def contar_vocales(cadena):
    ans = 0
    for i in cadena:
        if i == ('a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U'):
            ans += 1
    return ans

def solucion_c(pila):
    aux = Pila()
    mx = 0 # contador de mas vocales
    while not pila.esvacia():
        cur = pila.eliminar()
        mx = max(mx, contar_vocales(cur.nombre))
        aux.adicionar(cur)

    while not aux.esvacia():
        cur = aux.eliminar()
        if(mx == contar_vocales(cur.nombre)):
            cur.mostrar()
        pila.adicionar(cur)

def solucion_d(pila):
    aux = Pila()
    sol = Pila()

    while not pila.esvacia():
        mx = 0 # contador de mas vocales
        while not pila.esvacia():
            cur = pila.eliminar()
            mx = max(mx, cur.edad)
            aux.adicionar(cur)

        while not aux.esvacia():
            cur = aux.eliminar()
            if(mx == cur.edad):
                sol.adicionar(cur)
            else:
                pila.adicionar(cur)
    sol.mostrar();
    # pila.mostrar()


def solucion_e(pila, edad):
    aux = Pila()
    while not pila.esvacia():
        cur = pila.eliminar()
        if cur.edad > edad:
            aux.adicionar(cur)
    pila.vaciar(aux)
    pila.mostrar()

# Testing the Pila class
pila = Pila()
pila.adicionar(Estudiante("Bob", 25))
pila.adicionar(Estudiante("Alan", 22))
pila.adicionar(Estudiante("Maria", 45))
pila.adicionar(Estudiante("Elvis", 20))
pila.adicionar(Estudiante("Jose", 30))
pila.adicionar(Estudiante("Rafael", 45))
pila.mostrar()


# mostrar al estudiante mayor
print("Solucion A -> Estudiante mayor")
solucion_a(pila)

print("Solucion B -> Verificar si el estudiante X")
solucion_b(pila, "Bob")

print("Solucion C -> Mostrar al estudiante que tenga mas vocales en el nombre")
solucion_c(pila)

print("Solucion D -> ordenar la pila ascendentemente")
solucion_d(pila)

print("Solucion E -> Eliminar a los estudiantes con edad <= X")
solucion_e(pila, 30)


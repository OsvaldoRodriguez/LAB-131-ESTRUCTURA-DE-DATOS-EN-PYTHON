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

    def llenar(self, n):
        for i in range(1, n + 1):
            l = Estudiante()
            l.leer()
            self.adicionar(l)


class Estudiante:
    def __init__(self, ci=0, apellido="", nombre=""):
        self.ci = ci
        self.apellido = apellido
        self.nombre = nombre

    def getCi(self):
        return self.ci

    def setCi(self, ci):
        self.ci = ci

    def getApellido(self):
        return self.apellido

    def setApellido(self, apellido):
        self.apellido = apellido

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def mostrar(self):
        print("Estudiante")
        print("CI:", self.ci)
        print("APELLIDO:", self.apellido)
        print("NOMBRE:", self.nombre)
        print()

    def leer(self):
        print("ci - ap - nom")
        self.ci, self.apellido, self.nombre = input().split()
        self.ci = int(self.ci)



class MultiPila:
    def __init__(self):
        self.np = 0
        self.v = [Pila() for _ in range(100)]

    def getNp(self):
        return self.np

    def setNp(self, nc):
        self.np = nc

    def NroPilas(self):
        return self.np

    def nroelem(self, i):
        return self.v[i].nro_elem()

    def esvacia(self, i):
        return self.v[i].esvacia()

    def esllena(self, i):
        return self.v[i].esllena()

    def adicionar(self, i, L):
        if not self.v[i].esllena():
            self.v[i].adicionar(L)
        else:
            print(f"Pila {i} esta llena")

    def eliminar(self, i):
        e = Arbol()
        if not self.v[i].esvacia():
            e = self.v[i].eliminar()
        else:
            print(f"Pila {i} esta vacia")
        return e

    def llenar(self, n):
        self.np = n
        for i in range(1, n + 1):
            print(f"\nNro. elementos Pila {i}:")
            m = int(input())
            self.v[i].llenar(m)  # Aquí debes implementar el método llenar para la clase Pila

    def mostrar(self):
        for i in range(1, self.np + 1):
            print(f"\n\nDatos Pila {i}")
            self.v[i].mostrar()


def sol_a(multipila):

    for i in range(1, 1 + multipila.NroPilas()):
        print("pila ", i, "->")
        solucion_a(multipila.v[i])

def solucion_a(pila):
    aux = Pila()
    mx = 10**9 # edad maxima
    while not pila.esvacia():
        cur = pila.eliminar()
        mx = min(mx, cur.ci)
        aux.adicionar(cur)

    while not aux.esvacia():
        cur = aux.eliminar()
        if(mx == cur.ci):
            cur.mostrar()
        pila.adicionar(cur)

def sol_b(multipila, nombre):
    for i in range(1, 1 + multipila.NroPilas()):
        print("pila ", i, "->")
        solucion_b(multipila.v[i], nombre)

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

def sol_c(multipila):
    for i in range(1, 1 + multipila.NroPilas()):
        print("pila ", i, "->")
        solucion_c(multipila.v[i])

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

def sol_d(multipila):
    for i in range(1, 1 + multipila.NroPilas()):
        print("pila ", i, "->")
        solucion_d(multipila.v[i])


def solucion_d(pila):
    aux = Pila()
    sol = Pila()

    while not pila.esvacia():
        mx = 0 # contador de mas vocales
        while not pila.esvacia():
            cur = pila.eliminar()
            mx = max(mx, cur.ci)
            aux.adicionar(cur)

        while not aux.esvacia():
            cur = aux.eliminar()
            if(mx == cur.ci):
                sol.adicionar(cur)
            else:
                pila.adicionar(cur)
    sol.mostrar()
    pila.vaciar(sol)

def sol_e(multipila, ci):
    for i in range(1, 1 + multipila.NroPilas()):
        print("pila ", i, "->")
        solucion_e(multipila.v[i], ci)

def solucion_e(pila, ci):
    aux = Pila()
    while not pila.esvacia():
        cur = pila.eliminar()
        if cur.ci > ci:
            aux.adicionar(cur)
    pila.vaciar(aux)
    pila.mostrar()


multipila = MultiPila()
multipila.llenar(2)
multipila.mostrar()


# mostrar al estudiante mayor
print("Solucion A")
sol_a(multipila)

print("Solucion B ->")
sol_b(multipila, "Osvaldo")

print("Solucion C")
sol_c(multipila)

print("Solucion D")
sol_d(multipila)

print("Solucion E ->")
sol_e(multipila, 3000)

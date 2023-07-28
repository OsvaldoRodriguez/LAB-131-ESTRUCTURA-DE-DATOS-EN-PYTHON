class Estudiante:
    def __init__(self, ci=0, apellido="", nombre="", nota=0):
        self.ci = ci
        self.apellido = apellido
        self.nombre = nombre
        self.nota = nota

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

    def getNota(self):
        return self.nota

    def setNota(self, nota):
        self.nota = nota

    def mostrar(self):
        print("Estudiante")
        print("CI:", self.ci)
        print("APELLIDO:", self.apellido)
        print("NOMBRE:", self.nombre)
        print("NOTA:", self.nota)
        print()

    def leer(self):
        print("ci - ap - nom")
        self.ci, self.apellido, self.nombre, self.nota = input().split()
        self.ci = int(self.ci)
        self.nota = int(self.nota)


class NodoLS:
    def __init__(self):
        self.sig = None
        self.e = None

    def getSig(self):
        return self.sig

    def setSig(self, sig):
        self.sig = sig

    def getE(self):
        return self.e

    def setE(self, e):
        self.e = e


class ListaSimple:
    def __init__(self):
        self.p = None

    def getP(self):
        return self.p

    def setP(self, p):
        self.p = p

    def adicionar(self, e):
        cur = NodoLS()
        cur.setE(e)
        if self.getP() is None:
            self.setP(cur)
        else:
            q = self.getP()
            while q.getSig() is not None:
                q = q.getSig()

            q.setSig(cur)

    def mostrar(self):
        cur = self.getP()
        print("DATOS LISTA SIMPLE")
        while cur is not None:
            e = cur.getE()
            e.mostrar()
            cur = cur.getSig()

    def eliminar(self, ci):
        cur = self.getP()
        last = cur

        while cur is not None:
            e = cur.getE()
            if e.getCi() == ci:
                if cur == self.getP():
                    cur = cur.getSig()
                    self.setP(cur)
                    last = cur
                else:
                    last.setSig(cur.getSig())
                    cur = cur.getSig()
            else:
                last = cur
                cur = cur.getSig()

def solucion_a(lista):
    cur = lista.getP()
    mx = 0
    while cur is not None:
        e = cur.getE()
        mx = max(mx, e.getNota())
        cur = cur.getSig()
    cur = lista.getP()

    while cur is not None:
        e = cur.getE()
        if(mx == e.getNota()):
            e.mostrar()
        cur = cur.getSig()

def solucion_b(lista):
    cur = lista.getP()
    contador = 0
    while cur is not None:
        e = cur.getE()
        if e.getNota() < 51:
            contador += 1
        cur = cur.getSig()
    print("reprobaron", contador, "estudiantes")

def solucion_c(lista, ci, nota):
    cur = lista.getP()
    while cur is not None:
        e = cur.getE()
        if e.getCi() == ci:
            e.setNota(nota)
        cur = cur.getSig()
    lista.mostrar()


def solucion_d(lista, apellido):
    cur = lista.getP()
    contador = 0
    while cur is not None:
        e = cur.getE()
        if e.getApellido() == apellido:
            if e.getNota() > 50:
                contador += 1
        cur = cur.getSig()
    print("aprobaron", contador, "estudiantes")


def solucion_e(lista):
    cur = lista.getP()
    last = lista.getP()
    contador = 0
    while cur is not None:
        e = cur.getE()
        
        if e.getNota() < 51:
            if cur == lista.getP():
                lista.setP(cur.getSig())
                cur = cur.getSig()
                last = cur
            else:
                last.setSig(cur.getSig())
                cur = cur.getSig()
        else:
            last = cur
            cur = cur.getSig()
    lista.mostrar()

    
    

lista = ListaSimple()
lista.adicionar(Estudiante(345, "Rodriguez", "Osvaldo", 100))
lista.adicionar(Estudiante(22345, "Rodriguez", "Oliver", 90))
lista.adicionar(Estudiante(42345, "Apaza", "Alan", 23))
lista.adicionar(Estudiante(562345, "Mamani", "Roberto", 100))
lista.adicionar(Estudiante(32345, "Rodriguez", "Nelson", 12))
lista.adicionar(Estudiante(145645, "Quispe", "Ramiro", 0))
lista.adicionar(Estudiante(454345, "Moto", "Joaquin", 34))
lista.mostrar()

print("Solucion A")
solucion_a(lista)

print("Solucion B")
solucion_b(lista)

print("Solucion C")
solucion_c(lista, 145645, 99)

print("Solucion D")
solucion_d(lista, "Rodriguez")

print("Solucion E")
solucion_e(lista)


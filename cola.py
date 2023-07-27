class Estudiante:
    def __init__(self, ci, nombre, apellido):
        self.ci = ci
        self.apellido = apellido
        self.nombre = nombre

    def mostrar(self):
        print(f"CI: {self.ci}, APELLIDO: {self.apellido}, NOMBRE: {self.nombre}")


class ColaSimple:
    def __init__(self):
        self.ini = self.fin = 0
        self.max = 100
        self.A = [None] * (self.max + 1)

    def esvacia(self):
        return self.ini == 0 and self.fin == 0

    def esllena(self):
        return self.fin == self.max

    def nroelem(self):
        return self.fin - self.ini

    def adicionar(self, x):
        if not self.esllena():
            self.fin += 1
            self.A[self.fin] = x
        else:
            print("Cola llena")

    def eliminar(self):
        cur = None
        if not self.esvacia():
            self.ini += 1
            cur = self.A[self.ini]
            if self.ini == self.fin:
                self.ini = self.fin = 0
        else:
            print("cola vacia")
        return cur

    def vaciar(self, x):
        while not x.esvacia():
            self.adicionar(x.eliminar())

    def mostrar(self):
        aux = ColaSimple()
        if self.esvacia():
            print("cola simple vacia")
        else:
            while not self.esvacia():
                cur = self.eliminar()
                aux.adicionar(cur)
                cur.mostrar()
            self.vaciar(aux)

def solucion_a(cola):
    aux = ColaSimple()
    mx = 10**9 # edad maxima
    while not cola.esvacia():
        cur = cola.eliminar()
        mx = min(mx, cur.ci)
        aux.adicionar(cur)

    while not aux.esvacia():
        cur = aux.eliminar()
        if(mx == cur.ci):
            cur.mostrar()
        cola.adicionar(cur)

def solucion_b(cola, nombre, apellido):
    aux = ColaSimple()
    flag = False
    while not cola.esvacia():
        cur = cola.eliminar()
        if cur.nombre == nombre and cur.apellido == apellido:
            flag = True
        aux.adicionar(cur)
    cola.vaciar(aux)
    if flag == True:
        print('si existe')
    else:
        print("no existe")

def primo(x):
    if x == 2:
        return True
    if x < 2 or x % 2 == 0:
        return False

    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2

    return True
def solucion_c(cola):
    aux = ColaSimple()
    ans = 0
    while not cola.esvacia():
        cur = cola.eliminar()
        if primo(cur.ci):
            ans += 1
        aux.adicionar(cur)
    cola.vaciar(aux)
    print("son", ans, "estudiantes")


def solucion_d(cola):
    aux = ColaSimple()
    sol = ColaSimple()

    while not cola.esvacia():
        mn = 10**8 # contador de mas vocales
        while not cola.esvacia():
            cur = cola.eliminar()
            mn = min(mn, cur.ci)
            aux.adicionar(cur)

        while not aux.esvacia():
            cur = aux.eliminar()
            if(mn == cur.ci):
                sol.adicionar(cur)
            else:
                cola.adicionar(cur)
    sol.mostrar();
    cola.vaciar(sol);

    # cola.mostrar()


def solucion_e(cola, apellido):
    aux = ColaSimple()
    while not cola.esvacia():
        cur = cola.eliminar()
        # cur.mostrar()
        if cur.apellido != apellido:
            aux.adicionar(cur)
    cola.vaciar(aux)
    cola.mostrar()

cola = ColaSimple()
cola.adicionar(Estudiante(123, "Bob", "Quispe"))
cola.adicionar(Estudiante(331, "Alan", "Apaza"))
cola.adicionar(Estudiante(1232, "Maria", "Rodriguez"))
cola.adicionar(Estudiante(34545, "Elvis", "Mamani"))
cola.adicionar(Estudiante(1232, "Jose", "Delgado"))
cola.adicionar(Estudiante(34545, "Rafael", "Leon"))
cola.adicionar(Estudiante(34545, "Elena", "Leon"))
cola.adicionar(Estudiante(34545, "Robert", "Leon"))
cola.mostrar()


# mostrar al estudiante mayor
print("Solucion A -> Estudiante que tenga el menor CI")
solucion_a(cola)

print("Solucion B -> Verificar si el estudiante X")
solucion_b(cola, "Bob", "Quispe")

print("Solucion C -> Contar cuantos estudiantes tienen un CI primo")
solucion_c(cola)

print("Solucion D -> ordenar la pila ascendentemente")
solucion_d(cola)

print("Solucion E -> Eliminar a los estudiantes con apellido X")
solucion_e(cola, "Leon")


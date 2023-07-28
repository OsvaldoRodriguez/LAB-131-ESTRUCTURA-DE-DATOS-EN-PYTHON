class Futbolista:
    def __init__(self, nombre, edad, equipo, posicion):
        self._nombre = nombre
        self._edad = edad
        self._equipo = equipo
        self._posicion = posicion

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getEquipo(self):
        return self._equipo

    def setEquipo(self, equipo):
        self._equipo = equipo

    def getPosicion(self):
        return self._posicion

    def setPosicion(self, posicion):
        self._posicion = posicion

    def leer_datos(self):
        self._nombre = input("Nombre del futbolista: ")
        self._edad = int(input("Edad del futbolista: "))
        self._equipo = input("Equipo del futbolista: ")
        self._posicion = input("Posición del futbolista: ")

    # Método para mostrar los datos del futbolista
    def mostrar_datos(self):
        print("Nombre:", self._nombre)
        print("Edad:", self._edad)
        print("Equipo:", self._equipo)
        print("Posición:", self._posicion)
        print("---------------------------------------")


class NodoLD:
    def __init__(self):
        self._sig = None
        self._ant = None
        self._e = None

    def getSig(self):
        return self._sig

    def setSig(self, sig):
        self._sig = sig

    def getAnt(self):
        return self._ant

    def setAnt(self, ant):
        self._ant = ant

    def getE(self):
        return self._e

    def setE(self, e):
        self._e = e


class ListaDoble:
    def __init__(self):
        self._p = None

    def getP(self):
        return self._p

    def setP(self, p):
        self._p = p

    def adicionar(self, futbolista):
        cur = NodoLD()
        cur.setE(futbolista)

        q = self.getP()
        if q is None:
            self.setP(cur)
        else:
            while q.getSig() is not None:
                q = q.getSig()
            q.setSig(cur)
            cur.setAnt(q)

    def mostrar(self):
        print("LISTA DOBLE")
        q = self.getP()
        while q is not None:
            futbolista = q.getE()
            futbolista.mostrar_datos()
            q = q.getSig()

def solucion_a(lista_doble, posicion):
    print(posicion)
    q = lista_doble.getP()
    while q is not None:
        futbolista = q.getE()
        if futbolista.getPosicion().lower() == posicion.lower():
            futbolista.mostrar_datos()
        q = q.getSig()

def solucion_b(lista_doble):
    print("CAMBIAR A ARQUERO")
    q = lista_doble.getP()
    while q is not None:
        futbolista = q.getE()
        primer_caracter = futbolista.getNombre()[0].lower()
        if primer_caracter in "aeiouáéíóú":
            futbolista.setPosicion("Arquero")
        q = q.getSig()

    lista_doble.mostrar()


def solucion_c(lista_doble):
    print("ORDENAR POR EDAD")
    p = lista_doble.getP()
    while p is not None:
        minimo = p
        q = p.getSig()
        while q is not None:
            if q.getE().getEdad() < minimo.getE().getEdad():
                minimo = q
            q = q.getSig()
        
        if minimo != p:
            intercambiar(p, minimo)

        p = p.getSig()

    lista_doble.mostrar()

def intercambiar(nodo1, nodo2):
    temp = nodo1.getE()
    nodo1.setE(nodo2.getE())
    nodo2.setE(temp)


def solucion_d(self):
    posiciones = []
    contador = []

    q = self.getP()

    while q is not None:
        posicion = q.getE().getPosicion()
        if posicion in posiciones:
            index = posiciones.index(posicion)
            contador[index] += 1
        else:
            posiciones.append(posicion)
            contador.append(1)

        q = q.getSig()

    print("Cantidad de futbolistas por posición:")
    for i in range(len(posiciones)):    
        print(f"{posiciones[i]}: {contador[i]}")



def solucion_e(lista_doble):
    q = lista_doble.getP()
    while q is not None:
        if q.getE().getPosicion().lower() == "Delantero".lower():
            eliminar_futbolista(lista_doble, q)
        q = q.getSig()
    lista_doble.mostrar()

def eliminar_futbolista(lista_doble, futbolista_a_eliminar):
    q = lista_doble.getP()
    while q is not None:
        if q == futbolista_a_eliminar:
            if q.getAnt() is not None:
                q.getAnt().setSig(q.getSig())
            else:
                lista_doble.setP(q.getSig())

            if q.getSig() is not None:
                q.getSig().setAnt(q.getAnt())

            break

        q = q.getSig()


# Crear una instancia de la lista doble
lista_doble = ListaDoble()
# Agregar futbolistas a la lista
lista_doble.adicionar(Futbolista("Lionel Messi", 34, "Paris Saint-Germain", "Delantero"))
lista_doble.adicionar(Futbolista("Cristiano Ronaldo", 36, "Manchester United", "Delantero"))
lista_doble.adicionar(Futbolista("Neymar Jr", 29, "Paris Saint-Germain", "Delantero"))
lista_doble.adicionar(Futbolista("Robert Lewandowski", 32, "Bayern Munich", "Delantero"))
lista_doble.adicionar(Futbolista("Kylian Mbappe", 22, "Paris Saint-Germain", "Delantero"))
lista_doble.adicionar(Futbolista("Kevin De Bruyne", 30, "Manchester City", "Centrocampista"))
lista_doble.adicionar(Futbolista("Sergio Ramos", 35, "Paris Saint-Germain", "Defensa"))
lista_doble.adicionar(Futbolista("Jan Oblak", 28, "Atletico Madrid", "Portero"))
lista_doble.adicionar(Futbolista("Mohamed Salah", 29, "Liverpool", "Delantero"))
lista_doble.adicionar(Futbolista("Antoine Griezmann", 30, "Barcelona", "Delantero"))

# Mostrar la lista doble de futbolistas
lista_doble.mostrar()

print("SOLUCION A")
solucion_a(lista_doble, "defensa")
print("SOLUCION B")
solucion_b(lista_doble)
print("SOLUCION C")
solucion_c(lista_doble)
print("SOLUCION D")
solucion_d(lista_doble)
print("SOLUCION E")
solucion_e(lista_doble)


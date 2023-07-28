class Medallero:
    def __init__(self):
        pass

    # Implementar los métodos necesarios para la clase Medallero
    # Puedes basarte en la implementación que tengas en tu código original


class ColaCircularM:
    def __init__(self):
        self.max = 100
        self.v = [None] * (self.max + 1)
        self.ini = self.fin = 0

    def nroelem(self):
        return (self.max + self.fin - self.ini) % self.max

    def esvacia(self):
        return self.nroelem() == 0

    def esllena(self):
        return self.nroelem() == self.max - 1

    def adicionar(self, elem):
        if not self.esllena():
            self.fin = (self.fin + 1) % self.max
            self.v[self.fin] = elem
        else:
            print("Cola circular llena")

    def eliminar(self):
        elem = Medallero()
        if not self.esvacia():
            self.ini = (self.ini + 1) % self.max
            elem = self.v[self.ini]
            if self.nroelem() == 0:
                self.ini = self.fin = 0
        else:
            print("Cola circular vacia")
        return elem

    def mostrar(self):
        elem = Medallero()
        if self.esvacia():
            print("Cola vacia xxx")
        else:
            print("\n Datos de la Cola ")
            aux = ColaCircularM()
            while not self.esvacia():
                elem = self.eliminar()
                aux.adicionar(elem)
                elem.mostrar()
            while not aux.esvacia():
                elem = aux.eliminar()
                self.adicionar(elem)


class MultiColaCircularM:
    def __init__(self):
        self.nc = 0
        self.v = [ColaCircularM() for _ in range(30)]

    def NroColas(self):
        return self.nc

    def esvacia(self, i):
        return self.v[i].esvacia()

    def esllena(self, i):
        return self.v[i].esllena()

    def adicionar(self, i, elem):
        if not self.v[i].esllena():
            self.v[i].adicionar(elem)
        else:
            print(f"Cola {i} esta llena")

    def eliminar(self, i):
        e = Medallero()
        if not self.v[i].esvacia():
            e = self.v[i].eliminar()
        else:
            print(f"Cola {i} esta vacia")
        return e

    def llenar(self, n):
        self.nc = n
        for i in range(1, n + 1):
            print(f"Nro. elementos Cola Simple {i}:")
            m = int(input())
            self.v[i].llenar(m)  # Aquí debes implementar el método llenar para la clase ColaCircularM

    def mostrar(self):
        print("--------------------------")
        print("DATOS DE LA MULTIPLE COLA SIMPLE")
        print("--------------------------")
        for i in range(1, self.nc + 1):
            print(f"\n\nDatos Cola Simple {i}")
            self.v[i].mostrar()

    def mostrar(self, i):
        self.v[i].mostrar()

    def nroElem(self, i):
        return self.v[i].nroelem()

    def vaciar(self, i, z):
        self.v[i].vaciar(z)

    def vaciar(self, i, j):
        self.v[i].vaciar(self.v[j])

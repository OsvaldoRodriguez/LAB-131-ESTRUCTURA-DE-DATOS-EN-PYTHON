class Estudiante:
    def __init__(self, ci, nombre, edad, carrera):
        self._ci = ci
        self._nombre = nombre
        self._edad = edad
        self._carrera = carrera

    def getCi(self):
        return self._ci

class Nodo:
    def __init__(self, estudiante):
        self._estudiante = estudiante
        self._siguiente = None

    def getEstudiante(self):
        return self._estudiante

    def getSig(self):
        return self._siguiente

class ListaSimple:
    def __init__(self):
        self._inicio = None

    def adicionar(self, estudiante):
        nuevo_nodo = Nodo(estudiante)
        if self._inicio is None:
            self._inicio = nuevo_nodo
        else:
            nodo_actual = self._inicio
            while nodo_actual.getSig() is not None:
                nodo_actual = nodo_actual.getSig()
            nodo_actual._siguiente = nuevo_nodo

    def mostrar_por_ci(self, ci, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self._inicio

        if nodo_actual is None:
            print("No se encontró al estudiante con el CI:", ci)
            return

        estudiante = nodo_actual.getEstudiante()
        if estudiante.getCi() == ci:
            print("Estudiante encontrado:")
            print("CI:", estudiante.getCi())
            print("Nombre:", estudiante._nombre)
            print("Edad:", estudiante._edad)
            print("Carrera:", estudiante._carrera)
            return

        self.mostrar_por_ci(ci, nodo_actual.getSig())

    def eliminar_por_ci(self, ci, nodo_actual=None, nodo_anterior=None):
        if nodo_actual is None:
            nodo_actual = self._inicio

        if nodo_actual is None:
            print("No se encontró al estudiante con el CI:", ci)
            return

        estudiante = nodo_actual.getEstudiante()
        if estudiante.getCi() == ci:
            # Si encontramos al estudiante con el CI buscado, lo eliminamos
            if nodo_anterior is None:
                # Si el nodo a eliminar es el inicio de la lista
                self._inicio = nodo_actual.getSig()
            else:
                # Si el nodo a eliminar no es el inicio de la lista
                nodo_anterior._siguiente = nodo_actual.getSig()

            print("Estudiante eliminado:")
            print("CI:", estudiante.getCi())
            print("Nombre:", estudiante._nombre)
            print("Edad:", estudiante._edad)
            print("Carrera:", estudiante._carrera)
            return

        self.eliminar_por_ci(ci, nodo_actual.getSig(), nodo_actual)


lista_estudiantes = ListaSimple()
estudiante1 = Estudiante("12345", "Juan", 20, "Informática")
estudiante2 = Estudiante("67890", "María", 22, "Ingeniería Civil")
estudiante3 = Estudiante("54321", "Carlos", 21, "Arquitectura")

lista_estudiantes.adicionar(estudiante1)
lista_estudiantes.adicionar(estudiante2)
lista_estudiantes.adicionar(estudiante3)

ci_buscado = "67890"
lista_estudiantes.mostrar_por_ci(ci_buscado)
lista_estudiantes.eliminar_por_ci(ci_buscado)

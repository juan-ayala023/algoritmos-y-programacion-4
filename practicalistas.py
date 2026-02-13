class nodo:
    def __init__(self, documento, nombre):
        self.documento = documento
        self.nombre = nombre
        self.siguiente = None

class lista:
    def __init__(self):
        self.cabeza = None

    def agregarAlFinal(self, documento, nombre):
        nodo_ = nodo(documento, nombre)

        if self.cabeza == None:
            self.cabeza = nodo_

        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo_

from dataclasses import dataclass
from typing import List

@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

class Conjunto:
    contador = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.__id = Conjunto.contador
        Conjunto.contador += 1
        self.elementos = []

    @property
    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(e == elemento for e in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNION {otro_conjunto.nombre}")
        for elemento in self.elementos + otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __add__(self, otro_conjunto):
        return self.unir(otro_conjunto)

    def intersectar(self, other_conjunto):
        elementos_interseccion = [elemento for elemento in self.elementos if other_conjunto.contiene(elemento)]
        nombre_resultante = f"{self.nombre} INTERSECTADO {other_conjunto.nombre}"
        nuevo_conjunto = Conjunto(nombre_resultante)
        nuevo_conjunto.elementos = elementos_interseccion
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ", ".join(e.nombre for e in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"


# Crear elementos
elemento1 = Elemento("A")
elemento2 = Elemento("B")
elemento3 = Elemento("C")

# Crear conjuntos
conjunto1 = Conjunto("N1")
conjunto2 = Conjunto("N2")

# Agregar elementos a los conjuntos
conjunto1.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento3)

print(conjunto1)
print(conjunto2, "\n")

# Union de conjuntos
union_conjuntos = conjunto1 + conjunto2
print(union_conjuntos, "\n")

# Interseccion de conjuntos
interseccion_conjuntos = conjunto1.intersectar(conjunto2)
print(interseccion_conjuntos, "\n")

print(conjunto1.id)
print(conjunto2.id)

conjunto1.id = 5
print(conjunto1)
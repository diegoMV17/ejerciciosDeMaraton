class MatrizGrafo:
    def __init__(self):
        # Matriz de adyacencia (del documento)
        self.m = [
            [0,1,0,0,0,1,0,0,0],
            [1,0,1,1,1,1,0,0,0],
            [0,1,0,1,0,0,0,0,0],
            [0,1,1,0,1,0,1,1,0],
            [0,1,0,1,0,0,0,0,0],
            [1,1,0,0,0,0,0,1,1],
            [0,0,0,1,0,0,0,1,0],
            [0,0,0,1,0,1,1,0,1],
            [0,0,0,0,0,1,0,1,0]
        ]
        n = len(self.m)
        self.m1 = [[0]*n for _ in range(n)]
        self.mr = [[0]*n for _ in range(n)]

    def imprimir_matriz(self, matriz, titulo="Matriz"):
        print(f"\n{titulo}")
        for fila in matriz:
            print("\t".join(map(str, fila)))
        print()

    def obtener_matriz_orden_dos(self):
        """Calcula M^2 (caminos de longitud 2)."""
        n = len(self.m)
        # copiar m en m1
        for i in range(n):
            for j in range(n):
                self.m1[i][j] = self.m[i][j]

        # multiplicación m x m1
        for i in range(n):
            for j in range(n):
                self.mr[i][j] = 0
                for k in range(n):
                    self.mr[i][j] += self.m[i][k] * self.m1[k][j]

        self.imprimir_matriz(self.mr, "Matriz del Grafo Grado Dos (M^2)")

    def obtener_matriz_orden_tres(self):
        """Calcula M^3 (caminos de longitud 3)."""
        n = len(self.m)
        # copiar mr (M^2) en m1
        for i in range(n):
            for j in range(n):
                self.m1[i][j] = self.mr[i][j]

        # multiplicación m1 x m
        for i in range(n):
            for j in range(n):
                self.mr[i][j] = 0
                for k in range(n):
                    self.mr[i][j] += self.m1[i][k] * self.m[k][j]

        self.imprimir_matriz(self.mr, "Matriz del Grafo Grado Tres (M^3)")


class PruebaMatrizGrafo:
    def __init__(self):
        self.una_matriz_grafo = MatrizGrafo()

    def obtener_matriz(self):
        self.una_matriz_grafo.imprimir_matriz(self.una_matriz_grafo.m, "Matriz del Grafo (M)")
        self.una_matriz_grafo.obtener_matriz_orden_dos()
        self.una_matriz_grafo.obtener_matriz_orden_tres()


if __name__ == "__main__":
    prueba = PruebaMatrizGrafo()
    prueba.obtener_matriz()

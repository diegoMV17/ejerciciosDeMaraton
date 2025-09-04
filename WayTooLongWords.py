def toLongWay(palabras):
    for w in palabras:
        if len(w) <= 10:
            print(w)
        else:
            cantidadIntermedia = len(w) - 2
            print(f"{w[0]}{cantidadIntermedia}{w[-1]}")

if __name__ == "__main__":
    iteration = int(input())
    palabras = []

    for _ in range(iteration):
        palabra = input()
        palabras.append(palabra)
    toLongWay(palabras)
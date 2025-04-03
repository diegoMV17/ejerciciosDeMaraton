n = int(input())
palabras = []

for i in range(n):
    palabra = input()
    if len(palabra) > 10:
        abreviacion = f"{palabra[0]}{len(palabra) - 2}{palabra[-1]}"
        palabras.append(abreviacion)
    else:
        palabras.append(palabra)

for palabra in palabras:
    print(palabra)
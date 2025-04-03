palabra = input()
caracteres = len(palabra)
nuevaPalabra = ""
vocales = "aoyeui"
for i in range(0, caracteres):
    palabra = palabra.lower()
    if i > 0 and palabra[i] in vocales and palabra[i-1] in vocales:
        continue
    if palabra[i] not in vocales:
        nuevaPalabra += "."
        nuevaPalabra += palabra[i]
print(nuevaPalabra)
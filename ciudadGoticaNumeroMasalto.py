#Edificio mas alto en la ciudad gótica
iteration = int(input())
masalto = {}
altitud = []
for i in range(iteration):
    edificio = input()
    ed,al = edificio.split()
    al = int(al)
    if al not in masalto:
        masalto[al] = ed
        altitud.append(al)
    else:
        masalto[al] = max(masalto[al], ed)
print(masalto[max(altitud)])
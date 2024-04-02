#DESAFÍO VI: ¿Qué hace distintos a dos individuos de una especie? Propone una forma de 
#corroborar tu respuesta realizando un diagrama de un posible método computacional para 
#dicho fin.

#La diferencia típica dentro de una especie, incluidos los humanos, es 0,1 por ciento o 1 
#de 1.000 de los nucleótidos que componen una secuencia de ADN.

#!/usr/bin/env python3
import sys

secuenciaADN1 = sys.argv[1]
secuenciaADN2 = sys.argv[2]

diferencias = []

for i in range(0, len(secuenciaADN1)):
    if (secuenciaAdn[i] != secuenciaADN2[i] ):
        diferncias.append(i)

if diferencias:
    print(diferencias)
else:
    print("Son la misma muestra de ADN")

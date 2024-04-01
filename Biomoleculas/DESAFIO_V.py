#DESAFÍO V: Escribí un scrip en Python que prediga la estructura secundaria que adoptará cada residuo (aminoácido) de la secuencia 
#proteica dada, especificandola como H (si es una hélice), B (si es una hoja beta plegada) y L (si es un bucle o loop).

#!/usr/bin/env python3
import sys


helice = "EALMQKRH" #['E','A','L','M','Q','K','R','H']

plegada = "VIYCWFT" #['V','I','Y','C','W','F','T']

loop = "GNPSD" #['G','N','P','S','D']


secuencia = sys.argv[1]


for r in secuencia:
    if (r in helice):
        secuencia = secuencia.replace(r,"H")
    elif (r in plegada):
        secuencia = secuencia.replace(r, "B")
    elif (r in loop):
        secuencia = secuencia.replace(r,"L")
        

print (f'{secuencia}')

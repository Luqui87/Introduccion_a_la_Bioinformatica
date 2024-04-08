#DESAFIO III: En muchos de los genes codificados en el ADN existe un motivo recurrente ubicado antes de la secuencia codificante
#del gen que direcciona la unión de la ARN Polimerasa II, la proteína encargada de copiar el ADN a un ARN mensajero. Ésta secuencia 
#denominada caja TATA (consistente en una secuencia de nucleótidos 'TATAAA') se encuentra presente en lo que se denomina región promotora
#de diversos genes, en organismos de todos los reinos (Smale and Kadonaga 2003; Lifton et al. 1978)

# Creá un script en Python que, tomando como input un archivo con una secuencia de ADN, permita identificar las regiones promotoras
#de un gen, considerando que tal región comienza y termina con la caja TATA.

#!/usr/bin/env python3
import argparse
import re

parser = argparse.ArgumentParser(description='Identifica las regiones promoteres de un gen dada una secuencia de ADN')
parser.add_argument('-f', '--file',
                    type=str,
                    help='DNA secuence file')

args = parser.parse_args()


file = open(args.file , "r")
secuence = file.readline()

matches = re.findall(r'TATAA(.+?)TATAA',secuence)


print(matches)
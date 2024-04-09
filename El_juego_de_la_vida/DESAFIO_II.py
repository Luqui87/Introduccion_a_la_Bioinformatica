# DESAFIO II: Dado el código genético como se muestra en la tabla:
#Crea un script en Python que tome como argumento una secuencia proteica e imprima una cadena de ARN codificante. Podés usar de 
#ejemplo el siguiente péptido (cadena corta de aminoácidos):

#Sec1: ‘ATVEKGGKHKTGPNEKGKKIFVQKCSQCHTVLHGLFGRKTGQA'


#!/usr/bin/env python3
import argparse
import random

parser = argparse.ArgumentParser(description='Dada una secuencia proteica imprime la cadena ARN de dicho peptido')
parser.add_argument('-s', '--secuence',
                    type=str,
                    help='Aminoacids secuence')

args = parser.parse_args()
 
aminoacidos = [('F',["UUU","UUC"]),
        ('L' ,["UUA","UUG","CUU","CUC","CUA","CUG"]),
        ('I',["ISO","AUU","AUC","AUA"]),
        ('M',["AUG"]),
        ('V',["GUU", "GUC","GUA","GUG"]),
        ('S',["UCU", "UCC", "UCA", "UCG"]),
        ('P',["CUU", "CCC", "CCA", "CCG"]),
        ('T',["ACU", "ACC", "ACA", "ACG"]),
        ('A',["GCU", "GCC","GCA", "GCG"]),
        ('Y',["UAU", "UAC"]),
        ('H',[ "CAU", "CAC"]),
        ('Q',["CAA", "CAG"]),
        ('N',["AAU","ACC"]),
        ('K',["AAA","AAG"]),
        ('D',["GAU","GAC"]),
        ('E',["GAA","GAG"]),
        ('C',[ "UGU","UGC"]),
        ('W',["UGG"]),
        ('R',["CGU", "CGC","CGA","CGG","AGA","AGG"]),
        ('S',["AGU","AGC,"]),
        ('G',["GGU","GGC","GGA","GGG"]) ]

cadena = ""

def aRNOf(aminoacido):
    for a in aminoacidos:
        if (aminoacido == a[0]):
            return random.choice(a[1])
            break

for a in args.secuence:
    cadena = cadena + aRNOf(a)

print(cadena)
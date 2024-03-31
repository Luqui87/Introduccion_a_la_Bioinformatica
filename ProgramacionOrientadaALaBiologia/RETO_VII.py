#RETO VII: Ya que encontramos el espécimen de rana con pelo en marte, nos gustaría contrastar sus características con las ranas terrestres.
#Sabiendo que el gen de la proteína diminuta es ‘ATGGAAGTTGGAATCCAAGTTGGA’ y el gen de una proteína similar de rana terrestre 
#es ‘ATGGAAGTTAATGGAAGTTGGAGGAGA’ ¿podés crear un programa que compare la longitud de ambos genes y según cuál sea más grande 
#nos imprima un mensaje informándonos
#el resultado?

genDiminuta = "ATGGAAGTTGGAATCCAAGTTGGA"
genTerrestre = "ATGGAAGTTAATGGAAGTTGGAGGAGA"

if (genDiminuta > genTerrestre):
    print("El gen de rana diminuta es mas grande que el de rana terrestre")
elif (genDiminuta == genTerrestre):
    print("Ambos genes son de igual tamaño")
else:
    print("El gen de rana terrestre es mas grande que el de rana dimuta")
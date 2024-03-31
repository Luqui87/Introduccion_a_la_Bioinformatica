#RETO V: La Asombrosa Maravillosa es nuestra valiente superheroína. Sus poderes son producto de mutaciones en un gen muy común, 
#cuya secuencia en la mayoría de las personas es 'ATGGAACTTGCAATCGAAGTTGGC'. A diferencia de nosotros, el gen mutado de
#la Asombrosa Maravillosa incluye la secuencia 'GTTTGTGGTTG' en su interior. La Asombrosa Maravillosa adquirió sus poderes al
#beber Jugo Vencido. El primer sorbo de esta poción prohibida causa el cambio de todas las citosinas (C) por timinas (T). 
#El siguiente sorbo cambia todas las adeninas (A) por guaninas (G). El tercer sorbo cambia las citosinas (C) por adeninas (A). 
#El cuarto sorbo... puede ser mortal. ¿Podés escribir un programa que nos diga cuántos sorbos de Jugo Vencido debe beber 
#un portador del gen normal, para ganar los poderes de la Asombrosa Maravillosa?

secuencia = "ATGGAACTTGCAATCGAAGTTGGC"
genAsombrosaMaravillosa = "GTTTGTGGTTG"

secuencia = secuencia.replace('C','T')
primerSorbo = genAsombrosaMaravillosa in secuencia

secuencia = secuencia.replace('A','G')
segundoSorbo = genAsombrosaMaravillosa in secuencia

secuencia = secuencia.replace('C','A')
tercerSorbo = genAsombrosaMaravillosa in secuencia

print ((primerSorbo and 1) or (segundoSorbo and 2) or (tercerSorbo and 3) )




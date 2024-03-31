#RETO IX: Si ahora queremos hacer nuestro programa un poco más estricto, por cada vuelta deberíamos sumar el total de células 
#que tenemos e imprimir ese número en el mensaje. Entonces, por ejemplo, como en la primer vuelta tenemos dos células, imprimimos 
#como mensaje ‘¡Somos 2 clones!’ , pero en la segunda vuelta serán en total 4 células y el mensaje a imprimir debería ser 
#‘¡Somos 4 clones!’. ¿Podrías escribir esta modificación del programa?

celulas = 1

for i in range(1, 20):
    celulas *= 2
    print("Somos %s clones!", celulas)

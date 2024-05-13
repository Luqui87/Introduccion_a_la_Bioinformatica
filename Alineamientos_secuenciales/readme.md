>**PARA PENSAR** 🤔: ¿Qué tipo de información se puede extraer de la comparación de secuencias? ¿Cómo esperás que se vea en una comparación? 🤔

Se puede extraer información funcional de las proteínas, ídentificarlas por su presencia en otros organismo, evolutiva, se pueden interpretar las diferentes mutaciones que fueron ocurriendo a través del tiempo. Se ve a través de las similitudes que se encuentran en estas secuencias.

>**PARA PENSAR** 🤔: ¿Por qué crees que es mejor evaluar las relaciones evolutivas lejanas comparando proteínas? 🤔

Para poder comprender los diferentes cambios que fueron ocurriendo desde un antepasado en común. Así poder construir un arbol evolutivo que nos ayude a comprender la distancia entre dos especies.

>🧗🏻‍♀️DESAFIO I: Intentemos, entonces alinear estas dos palabras, para comprender mejor el problema. Alineá en la [tabla interactiva](https://flbulgarelli.github.io/umi/#una-palabra-no-dice-nada-y-al-mismo-tiempo-lo-dice-todo) las palabras "BANANA" y "MANZANA".  
>
>¡Tomá nota de tus observaciones y de las conclusiones que se desprendan de estas observaciones!
>☑️ PREGUNTAS DISPARADORAS: ¿Existe una única forma de alinearlas? ¿Es alguno de los posibles alineamientos mejor que otro? Si así fuera ¿Por qué?

No existe una única forma de alinearlas. Si hay mejores alineaminetos que otros ya que diferentes alieamientos tienen mas igualdades que otras.

>🧗🏻‍♀️DESAFIO II: En la siguiente [tabla interactiva](https://flbulgarelli.github.io/umi/#una-palabra-no-dice-nada-y-al-mismo-tiempo-lo-dice-todo)  distintos alineamientos para las palabras "ANA" y "ANANA". Verás que en el margen superior izquierdo aparece un valor de identidad calculado para cada alineamiento que intentes.
>
>¡Tomá nota de los valores de identidad observados y de las conclusiones que se desprendan de estas observaciones!
> 
>☑️ PREGUNTAS DISPARADORAS: ¿Son todos los valores iguales? ¿Qué consideraciones deberían tenerse en cuenta a la hora de realizar el cálculo? ¿Se te ocurre, distintas formas de calcularlo? ¿Serán todas ellas igualmente válidas en Biología?

Se debe tener en cuenta los gaps que se dejan en las secuencias y la penalización que tendran estos. Hay distintas formas de calcularlo, dependiendo del prioridad que se le de, ya sea a los gaps a la distancias química entre ácidos nucleicos. Dependerán de lo que se priorize para hallar el mejor puntaje.

>🧗🏻‍♀️DESAFIO III: Probá en  [tabla interactiva](https://flbulgarelli.github.io/umi/#una-palabra-no-dice-nada-y-al-mismo-tiempo-lo-dice-todo) distintos alineamientos para las palabras "ANA" y "ANANA". Verás que en el margen superior izquierdo aparece un valor de identidad calculado para cada alineamiento que intentes y un botón para cambiar la penalidad que se le otorga a dicho para el cálculo de identidad.
> 
>Probá varias combinaciones, tomá nota de los valores de identidad observados y de las conclusiones que se desprendan de estas observaciones.
>
>☑️ PREGUNTAS DISPARADORAS: ¿Cómo se relacionan los valores de identidad obtenidos con las penalizaciones que se imponen al gap? ¿Qué implicancias crees que tiene una mayor penalización de gaps? ¿Se te ocurre alguna otra forma de penalización que no haya sido tenido en cuenta en este ejemplo?

A mayor penalización menor es la identidad si se encuentran gaps. Si se busca una secuencia mas similar se aumentara la penalización de los gaps. Distancia entre letras que se comparan puede ser otra forma de penalización.

>**PARA PENSAR** 🤔: Entonces, pensando en un alineamiento de ácidos nucleicos ¿Cuáles te parece que son las implicancias de abrir un gap en el alineamiento? ¿Qué implicaría la inserción o deleción de una región de más de un residuo?

Las implicaciones de abrir un gap en el alinemamiento es que se cambia los aminoácidos que se terminan produciendo.

>🧗🏻‍♀️DESAFIO IV: Probá en la [tabla interactiva](https://flbulgarelli.github.io/umi/#una-palabra-no-dice-nada-y-al-mismo-tiempo-lo-dice-todo) distintos alineamientos para las secuencias nucleotídicas. Podrás ver las traducciones para cada secuencia.

>**PARA PENSAR** 🤔: ¿Dá lo mismo si el gap que introducís cae en la primera, segunda o tercer posición del codón? ¿Cómo ponderarías las observaciones de este ejercicio para evaluar el parecido entre dos secuencias?

No da lo mismo ya que los aminoácidos las tercera parte del condon puede cambiar y sigue siendo el mismo amino. Pero en cambio si cambiara la primera parte el aminoácido se transformaria en otro.


> **PARA PENSAR** 🤔: ¿En qué consiste la programación dinámica? ¿Por qué crees que es útil en este caso? 

La programación dinámica es una tecnica matemática que proporciona un procedimiento sistemático para encontrar la combinación de decisiones que maximice la efectividad total, al descomponer el problema en etapas, las que pueden ser completadas por una o más formas (estados), y enlazando cada etapa a través de cálculos recursivos. Es necesaria ya que tendremos que comparar las bifurcaciones que aparezcan al buscar el alineamiento con mejor puntaje.

>**PARA PENSAR** 🤔: ¿En qué casos serán de utilidad uno u otro tipo de alineamientos? ¿Qué limitaciones tendrá cada uno?

A pares sera mas efectiva si se quiere comparar una mutación en un individuo específico, nos permite comparar mas de cerca pero a su vez consume mas tiempo. Las de alineámiento multiple sirven para ver los cambios en una especie entera, nos permite ver un panaroma mas global de los cambios.

>**PARA PENSAR** 🤔: Ingresá al servidor del NCBI y mirá los distintos programas derivados del BLAST que se ofrecen ¿Para qué sirve cada uno? ¿En qué casos usarías cada uno?   
Nucletoide BLAST: Sirve para buscar secuencias de ácidos nucleicos homologas.
Protein BLAST: Sirve para buscar secuencias de aminoácidos homologas.
blastx: Traducir secuencias de ácidos nucleicos a secuencias proteícas y buscar homologas
tblastn: Lo inverso a blastx

>🧗🏻‍♀️DESAFIO VII: calculá el E-value y % identidad utilizando el programa Blast de la siguiente secuencia input usando 20000 hits, un e-value de 100 y tomando aquellos hits con un mínimo de 70% cobertura. Observe y discuta el comportamiento de : E-value vs. % id, Score vs % id,  Score vs E-value
>
>VVGGLGGYMLGSAMSRPIIHFGSDYEDRYYRENMHRYPNQVYYRPMDEYSNQNNFVHDCVNITIKQHTVTTTTKGENFTETDVKMMERVVEQMCITQYERESQAYYQRGSSMVLFSSPPVILLISFLIFLIVG

E-value vs %id
A mayor es el E-value menor es la identidad de la secuencia.

Score vs % id 
Se mantienen igualados, a mayor score, mayor es la identidad.

Score vs E-value
A mayor es el E-value menor es el score.


>🧗🏻‍♀️DESAFIO VIII: Realizá nuevas búsquedas usando la mitad de la secuencia problema y para un cuarto de la secuencia original. Compará los gráficos obtenidos. ¿Qué conclusiones puede sacas?
>Se mantienen los resultados excepto los scores y e-values que bajan

🧗🏻‍♀️DESAFIO IX: Utilizando BLAST utilice búsquedas de similitud secuencial para identificar a la siguiente proteína:
>
>MIDKSAFVHPTAIVEEGASIGANAHIGPFCIVGPHVEIGEGTVLKSHVVVNGHTKIGRDNEIYQFASIGEVNQDLKYAGEPTRVEIGDRNRIRESVTIHRGTVQGGGLTKVGSDNLLMINAHIAHDCTVGNRCILANNATLAGHVSVDDFAIIGGMTAVHQFCIIGAHVMVGGCSGVAQDVPPYVIAQGNHATPFGVNIEGLKRRGFSREAITAIRNAYKLIYRSGKTLDEVKPEIAELAETYPEVKAFTDFFARSTRGLIR

Acyl-(acyl-carrier-protein)—UDP-N-acetylglucosamine O-acyltransferase

>
>**PARA PENSAR** 🤔: ¿Cuál es la función de la proteína? ¿A qué grupo taxonómico pertenece? A un nivel de significancia estadística adecuado ¿cuántas secuencias similares se encuentran? 

Es una encima que cataliza una reacción química que es el primer paso de la biosintesis de lipidos A. the transfer of the R-3-hydroxyacyl chain from R-3-hydroxyacyl acyl carrier protein (ACP) to the glucosamine 3-OH group of UDP-GlcNAc. Pertenece al grupo taxonomico reiono.
Se encuentran cerca de 500 secuencias familiares.
>
>🧗🏻‍♀️DESAFIO X:  Realizá una nueva corrida del BLASTp, utilizando la misma secuencia , pero ahora contra la base de datos PDB.  ¿Se obtienen los mismos resultados? ¿Qué tipo de resultados(hits) se recuperan? ¿Cuándo nos podría ser útil este modo de corrida?

Hay una mucho menor cantidad de resultados. Cuando queremos buscar datos mas fiables o mas específicos.
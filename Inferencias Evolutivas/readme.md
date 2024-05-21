>
>🧗🏻‍♀️DESAFÍO I: Detalla las tácticas y/o metodologías que deberían utilizarse para darles una respuesta a los padres del niño. 
Dadas las secuencias de Mosca, humano y Moscahumano ¿Qué criterios se les ocurren para comparar las secuencias? ¿Qué resultados obtienen del análisis anterior?
¿Qué resultado esperaría obtener si utilizara el resto de las secuencias en el análisis? ¿Por qué? 
>

Se debe utilizar una herramienta como Blast para buscar secuencias homologas en una base de datos de la secuencia Cyt P450 extraída. Ya con estas puedo realizar alineamientos secuenciales.
Los criterios a tener en consideración para la comparación es una penalización de gap alta, para encontrar la secuencia mas similar. 
Se obtiene que es mayor el resultado del alineamiento con el humano que la mosca. En el arbol filogénico generado se muestra a cada secuencia como una rama de un ancestro en común. Si agregamos mas secuencias se ampliara el arbol, se armaran mas clavos y se podra extraer mas información del arbol evolutivo de la secuencias.

>🧗🏻‍♀️DESAFÍO II: Como vimos anteriormente existen algunos softwares optimizados para confeccionar alineamientos de secuencias. En particular hemos trabajado con [Clustal](https://www.ebi.ac.uk/Tools/msa/clustalo/) (Larkin et al. 2007). Confecciona el alineamiento para el punto I.
>

>🧗🏻‍♀️DESAFÍO III: Mediante el uso del servidor de [IQtree](http://iqtree.cibiv.univie.ac.at/) (Trifinopoulos et al. 2016), confecciona los árboles filogenéticos para los alineamientos obtenidos en el punto II.
Como vemos, el servidor nos permite elegir el modelo de sustitución ¿A qué se refiere?
¿Qué es el Bootstrap? ¿De qué manera nos habla de la calidad de nuestro árbol? ¿Cómo influye el número de Bootstraps en el resultado?
Interpreten los resultados obtenidos, mediante la visualización de los árboles con la herramienta [FigTree](http://tree.bio.ed.ac.uk/software/figtree/). ¿Es necesario realizar algún paso extra, previo a la interpretación del árbol? ¿Por qué? 
>

Refiere al modelo que usara para calcular la sustitución de un aminoácido por otro.
```
+----------------------------------------------------------Mosca
|
|          +**Humano
|       +--|
|       |  +**Chimpance
+-------|
|       |            +-----------Rana
|       |      +-----|
|       |      |     +----Gallo
|       +------|
|              |  +---Caballo
|              +--|
|                 +--Perro
|
+**Bartmosca
```

El bootsrapping es la creación de datos similares randomizados para obtener una mejor estimación. Mientras mas datos nuestro arbol tenga puede infererir mejor su esquema.
Para interpretar el árbol es necesario rootear el arbol con la especie mas alejada al grupo de interes. Se hace para lograr una mejor interpretación del árbol.

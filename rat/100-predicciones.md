# 100 predicciones.

Go [here](nunosempere.github.io/rat/100-predictions.html) for a version in English

## Día 1: Sábado 15 Sept / 2018.
{SHA es un acrónimo de Secure Hashing Algorithm; un algoritmo de hash recibe una cadena o un documento y devuelve un número.
Así, el hash de un documento puede ser revelado sin el documento, y si este se publica después, se sabe que es el verdadero.

En 2017, un projecto de Google y CWI Amsterdam ha producido dos pdfs distintos y legibles que tienen el mismo hash SHA1.  Esto hace al hash inseguro; el hash no es suficiente para identificar al documento. 

La familia continuó con SHA2, y ahora, SHA3. La versión más segura de este último es SHA3-512.

Preguntas: 
- ¿Qué probabilidad, por año, asignáis a que SHA3-512 sea exitosamente atacado?
Entendemos por exitosamente el que se encuentren dos x, x' tal que SHA3-512(x) = SHA3-512(x'), 
o bien que dado un y=SHA3-512(z), se encuentre un z' =/= tal que SHA3-512(z')=y.
- ¿Qué probabilidad, por año, le dáis a que SHA3-512 sea reemplazado?}  

Tiempo recomendado: 15 mins.

## Comentarios día 1.
Nuño: La frecuencia histórica de ataque exitoso es de 1/22, lo cual da un 5% / año.
Pero en el caso anterior hubo un goteo de resultados teóricos cada vez ms potentes, hasta llegar a alguno que se podía implementar, y no he visto en absoluto algo parecido para Kekkak (la familia a la que pertenece SHA-3).
Además, es un diseño relativamente nuevo. En los próximos años me extrañaría mucho que se atacara exitosamente antes de ver esas señales. De ahí el 1%.  
No obstante, luego he leído otro artículo que decía que SHA3 podría ser particularmente vulnerable a man-in-the middle attacks, porque algunos de sus pasos son biyecciones. Por lo tanto mi definición de ataque ha resultado inadecuada.  
De ahí que a la hora de reemplazarlo haya vuelto a frecuencias históricas. Escribiendo aquí esto, aún así me extrañaría mucho que se cambiase en los próximos 3 años, y lo bajo a un 6%. Como decía Nikolás, mis distribuciones no son planas: cuanto más tiempo pase, más probabilidad por año.  
Más adelante, sigo pensando que 6% es demasiado alto, ya que el proceso de aceptación de SHA3 duró de 2012 a 2015, es decir, 3 años, y el proceso para SHA4 no ha empezado todavía. La bajo entonces a 2-3% -> 2.5%

## Día 2. Martes 17 Sept 2018
{La reina de Inglaterra, Isabel II, nació en el año 1926, mientras que el antiguo rey de España, Juan Carlos I,  nació en 1938. 

Pregunta: 
- ¿Qué probabilidadle asignáis que Isabel II muera después que Juan Carlos I?}

## Discusión Día 2.
Las probabilidades del grupo se mueven de entre 6% (la mía) y 25%. Yo he obtenido la mía yendo a (tablas actuariales inglesas)[https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/lifeexpectancies/datasets/nationallifetablesunitedkingdomreferencetables], y mirando la esperanza de vida a 80 y a 92 años para hombres y mujeres. He creaso un modelo simplificado, en el que la reina era simplemente una paisana inglesa de 92 años, y el rey uno de 80.  
Con dichas tablas actuariales, es relativamente fácil calcular la probabilidad de que la reina siga viva dentro de X años, y de que el rey se muera justo dentro de X años. Sumando esto para cada año. obtengo la probabilidad de que la reina siga viva cuando el rey muere, en general.  Este modelo me da un 5,5575% de de que Isabel II muera después que Juan Carlos I.  He tenido que hacer una pequeña interpolación para obtener la probabilidad de muerte a edades de más de 100 años, pero su efecto es muy pequeño.  Más importante es que he tomado las probabilidades de 2016, y la esperanza de vida aumenta con el tiempo.  
Por otro lado, entiendo que ambos reyes tienen acceso a médicos mejores que los de la población general, pero el error afecta a ambos. No obstante, creo que los españoles son un poco peores. Además, Juan Carlos I se ha roto la cadera, mientras que la reina de Inglaterra no ha tenido incidentes parecidos. Por ello subo la probabilidad un poco, a un 6%.  
Si me interesara mucho el resultado, haría algunas simulaciones de Monte Carlo, y no por año, sino por semana / día (interpolando la probabilidad por semana).

## Día 3. Lunes 24 de Septiembre.
{El grupo de Altruismo Efectivo España se propuso dar una charla TedX. ¿Qué probabilidad le asignáis a que se lleve a cabo en 2019? Técnica: A veces es útil formular la pregunta en negativo: ¿qué probabilidad le dáis a que no se haga?}

## Lista de ideas:
- Precios, valores de cosas.
- Tempereatura media en España, GLobal, Inviertno.
- Número refugiados alemania.
- Premio Nobel / Medalla fields Africano.
- Soft Brexit. ¿Cómo operacionalizar?
- Crisis económica.
- Catástrofe con >= 10 personas muertas.
- Acciodente avión.
- Atentado terrorista=?
- Ventas X número de coches eléctricos en España.
- Probabilidad de que todos contesten a las 100 preguntas. Cada uno.
- Probabilidad lesión de Gareth Bale / Cristiano Ronaldo.
- Probabilidad de que Trump termine la legislatura.
- Probabilidad mantenerse en el poder de: Trump, Putin, Macron, Erdogan, Merkel.
- P de que Woody Allen saque película en 2019.
- El grupo de EA España no organizará una charla de TedX en 2019.

## Hashes.
Aquello que esté en paréntesis será hasheado con SHA3-512, y publicado en twitter bajo @NunoSempere.

### Día 1: 
29f91f9fa34dd74aa8fbbc7410920cb8a6aec28fd6248d4187f8a9a2608b0b0eab73c4e05dde0902ccb95cf26c3ef0a9057868865d3d7e6f5be7003190e0e3bc. 
Correcciones: z' =/= z.
Nota: SHA-3 se reemplaza se interpreta como que aparece un SHA-4.

## Día 2:
ce11fdf1500cd161e4c9432a990ae016943aed8e40e9611b8743efc7117da8ccdcc9614a72bcc9e6e44dce2e874eca328713a3496eff9d170fce383b47cde5a3

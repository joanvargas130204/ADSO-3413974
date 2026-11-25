# 8. Lista de chequeo de verificación

Estado tras la segunda verificación ([resultado](verificacion/resultado-verificacion-2.txt)). «1.ª» = resultado de la primera pasada.

| # | Grupo | Criterio | 1.ª | 2.ª |
|---|---|---|---|---|
| 1 | Cobertura | Los 54 RF aparecen en la matriz de trazabilidad | Cumple | Cumple |
| 2 | Trazabilidad | ≥ 90 % de los RF llegan a clase y entidad (49/54) | Cumple | Cumple |
| 3 | Trazabilidad | Toda clase de dominio y toda entidad del MER tiene al menos un requisito | Falla | Cumple |
| 4 | Trazabilidad | Las clases y entidades de la matriz existen en los modelos | Cumple | Cumple |
| 5 | Actividades | Hay 2 diagramas de actividades de casos críticos con fuente editable e imagen | Cumple | Cumple |
| 6 | Actividades | Todas las decisiones tienen guarda en cada salida | Cumple | Cumple |
| 7 | Actividades | Las ramas A/E del diagrama coinciden con las de la plantilla | Cumple | Cumple |
| 8 | Actividades | El orden de los pasos del diagrama coincide con el de la plantilla | Falla | Cumple |
| 9 | Plantillas | Cada plantilla tiene ≥ 6 pasos principales | Cumple | Cumple |
| 10 | Plantillas | Cada plantilla tiene ≥ 1 flujo alterno y ≥ 1 excepción con su paso de origen | Cumple | Cumple |
| 11 | Plantillas | Sin detalle de implementación (rutas, peticiones, tecnología) | Falla* | Cumple |
| 12 | Plantillas | Precondición, alterno y excepción están bien distinguidos | Cumple | Cumple |
| 13 | Dominio | ≥ 8 clases, ≥ 5 con 2 o más atributos, sin métodos ni claves foráneas | Falla | Cumple |
| 14 | Dominio | Hay generalización y clase de asociación | Cumple | Cumple |
| 15 | Dominio | Los conceptos que usan las plantillas existen como clase o atributo (stock, estado, puntos, dirección) | Falla | Cumple |
| 16 | MER | ≥ 6 entidades con PK y notación declarada (pata de gallo) | Cumple | Cumple |
| 17 | MER | Las N:M están resueltas con entidad asociativa con atributos | Cumple | Cumple |
| 18 | MER | Hay entidad débil o relación recursiva | Cumple | Cumple |
| 19 | Coherencia | Las relaciones del dominio coinciden con las del MER (Cliente–Nivel) | Falla | Cumple |
| 20 | Prototipo | ≥ 3 pantallas, cada una rotulada con el CU que atiende | Cumple | Cumple |
| 21 | Enlaces | Todos los enlaces relativos de los documentos son válidos | Cumple | Cumple |

\* Fila 11: la falla de la primera pasada fue un falso positivo del script (la palabra «Postcondiciones» coincidía con POST); se corrigió el script y las plantillas no cambiaron. Fila 13: la falla fue de la documentación (decía 16 clases con 2 o más atributos; son 13). Criterios de cobertura y trazabilidad: 1, 2, 3, 4 y 19.

Criterios de cobertura y trazabilidad: 1, 2, 3, 4 y 19 (5).

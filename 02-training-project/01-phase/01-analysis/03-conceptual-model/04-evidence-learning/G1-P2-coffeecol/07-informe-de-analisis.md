# 7. Informe de análisis (resumen para el instructor)

**Qué se verificó.** Que el modelo de análisis de CoffeeCol (casos de uso críticos CU-03, CU-06 y CU-11, dos diagramas de actividades, tres plantillas, modelo de dominio de 18 clases, MER de 15 entidades y tres pantallas) sea consistente entre sí y cubra los 54 requisitos funcionales del SRS. La verificación se hizo con una lista de 21 criterios ([08](08-lista-de-chequeo.md)) y con un script que revisa las reglas automáticamente ([verificar_consistencia.py](verificacion/verificar_consistencia.py)).

**Resultado de la primera verificación.** El script dio 39 chequeos correctos y 4 fallas; además, al releer el diagrama de iniciar sesión contra su plantilla encontré una quinta inconsistencia (el orden de los pasos). También corregí un falso positivo del propio script (confundía «Postcondiciones» con la palabra técnica POST). Detalle con antes y después en [09-registro-de-ajustes.md](09-registro-de-ajustes.md).

**Hallazgos principales corregidos.**
1. La clase Usuario no se trazaba a ningún requisito.
2. El modelo de dominio relacionaba Cliente con NivelFidelizacion, pero el MER deduce el nivel de los puntos y no tiene esa relación.
3. La plantilla de CU-11 permite retirar un producto, pero Producto no tenía un atributo de estado.
4. El diagrama de iniciar sesión pedía el método después de contactar al servicio externo y pasaba el enlace mágico por una aprobación que la plantilla no tiene.
5. La documentación decía que 16 clases tenían 2 o más atributos; en realidad son 13.

**Segunda verificación.** 43 chequeos correctos y 0 fallas ([resultado](verificacion/resultado-verificacion-2.txt)).

**Cobertura.** 49 de 54 requisitos (90,7 %) llegan hasta clase y entidad. Los 5 restantes (RF-001, 003, 005, 009, 010) son de presentación y no manejan datos; su exclusión está justificada en la [matriz](06-matriz-de-trazabilidad.md). Todos los requisitos se asocian a un caso de uso (54 de 54, ver G1-P1).

**Limitaciones.** Solo los tres casos críticos tienen plantilla y pantalla; los diagramas de actividades son secuenciales (sin concurrencia); el modelo no se ha validado con el cliente (Tantico Café) ni con el resto del equipo; el carrito queda fuera del MER porque el SRS lo guarda en el navegador.

**Decisión.** El modelo queda apto para pasar a diseño (G2), con las limitaciones anotadas.

# 9. Registro de ajustes (hallazgos de la verificación)

Cada hallazgo salió de la primera verificación ([resultado 1](verificacion/resultado-verificacion-1.txt)) o de una relectura cruzada y se comprobó en la segunda ([resultado 2](verificacion/resultado-verificacion-2.txt)).

| # | Hallazgo | Dónde | Antes | Después | Verificación 2 |
|---|---|---|---|---|---|
| 1 | La clase Usuario no tenía requisito asociado y la matriz afirmaba que ninguna clase quedaba sin requisito | `06-matriz-de-trazabilidad.md` | RF-023, 024, 027 y 028 se trazaban solo a Cliente (y Administrador) | Esos requisitos se trazan también a Usuario, que es la clase de la que heredan | Cumple |
| 2 | El dominio relacionaba Cliente con NivelFidelizacion (asociación 1..*) pero el MER no | `diagramas/modelo-dominio.mmd` | `Cliente "0..*" --> "1" NivelFidelizacion : se clasifica en` | Dependencia `Cliente ..> NivelFidelizacion : nivel deducido de sus puntos`, igual que el MER | Cumple |
| 3 | La plantilla CU-11 permite retirar un producto (A2) pero Producto no tenía atributo de estado | dominio y MER | Producto sin estado | Atributo `estado` en la clase Producto y en la entidad PRODUCTO | Cumple |
| 4 | El diagrama de iniciar sesión no seguía el orden de la plantilla: contactaba al servicio antes de preguntar el método, ponía esa decisión en la calle de Firebase y llevaba el enlace mágico por una aprobación que la plantilla no tiene (A1 salta al paso 7) | `diagramas/actividad-iniciar-sesion.mmd` | Elegir método → solicitar identidad → ¿responde? → ¿método? (en la calle de Firebase) | Elegir método → ¿método elegido? (calle Sistema) → [Google] solicitar identidad → ¿responde?; [enlace mágico] correo → enlace → validación | Revisión manual del diagrama, ramas A/E comprobadas por el script |
| 5 | El documento del dominio decía que 16 clases tenían 2 o más atributos | `03-modelo-de-dominio.md` | «en 16 clases» | «en 13 clases» y se nombran las 5 con un solo atributo | Cumple |
| 6 | El script marcaba como detalle técnico la palabra «Postcondiciones» (coincidía con POST) | `verificacion/verificar_consistencia.py` | Búsqueda sin límites de palabra y sin distinguir mayúsculas | Búsqueda con `\b` y sensible a mayúsculas | Cumple |

Resumen: 6 hallazgos (5 del modelo y 1 de la herramienta). Primera pasada: 39 correctos y 4 fallas automáticas (más el hallazgo 4, de relectura). Segunda pasada: 43 correctos, 0 fallas.

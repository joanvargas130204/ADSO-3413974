# Análisis y Propuesta de Solución — Sistema de Gestión de Horarios Académicos SENA

**Proyecto:** Sincronización Total: El Nuevo Motor de Horarios Académicos SENA  
**Autor:** Joan Sebastian Vargas RAmos 
**Ficha:** 3413974 
**Rol:** Desarrollador Full-Stack  

---

## Índice

1. Introducción
2. Problema identificado
3. Puntos críticos del proceso actual
4. Objetivo de la solución
5. Actores del sistema
6. Modelo actual vs. modelo propuesto
7. Arquitectura de la solución
8. Flujo general del sistema
9. Módulos principales
10. Historias de usuario
11. Propuesta UX/UI
12. Motor de validación
13. Indicadores y metas
14. Beneficios de la solución
15. Conclusiones

---

# 1. Introducción

El proyecto **Sistema de Gestión de Horarios Académicos SENA** propone una solución de software integral para mejorar la planificación, asignación y consulta de horarios dentro del ecosistema académico.

La propuesta parte de una problemática relacionada con la gestión manual de información de instructores, ambientes y fichas de formación. Cuando estos datos se encuentran dispersos en hojas de cálculo, documentos y diferentes medios de comunicación, la planificación se vuelve más lenta y aumenta la posibilidad de cometer errores.

La solución planteada centraliza la información y utiliza un **motor de validación automática** para detectar posibles conflictos antes de confirmar una asignación.

El propósito principal es pasar de un proceso dependiente de revisiones manuales a un proceso centralizado, automatizado y orientado a la prevención de errores.

---

# 2. Problema identificado

La gestión manual de horarios presenta dificultades cuando aumenta el volumen de información institucional.

## 2.1 Dispersión de información

Los datos relacionados con:

- Instructores.
- Ambientes.
- Fichas de formación.
- Bloques de horario.
- Disponibilidad.

pueden encontrarse distribuidos en hojas de cálculo, archivos y comunicaciones independientes.

Esta dispersión dificulta disponer de una única fuente de información actualizada.

## 2.2 Planificación manual

La asignación de espacios e instructores puede depender de revisiones visuales y de información que no necesariamente se encuentra actualizada.

Esto aumenta la posibilidad de realizar asignaciones incorrectas.

## 2.3 Conflictos durante la planificación

Los conflictos pueden producirse cuando:

- Dos fichas utilizan el mismo ambiente en el mismo horario.
- Un instructor es asignado a dos actividades simultáneamente.
- Una asignación se encuentra fuera de la disponibilidad del instructor.
- La cantidad de aprendices supera la capacidad del ambiente.

Cuando estos problemas se descubren después de realizar varias asignaciones, es necesario rehacer parte del proceso.

---

# 3. Puntos críticos del proceso actual

## 3.1 Conflictos de horarios

Es uno de los principales riesgos identificados.

Puede producirse un cruce cuando dos fichas de formación son asignadas al mismo ambiente o instructor durante el mismo bloque de tiempo.

### Consecuencia

El coordinador debe revisar y corregir manualmente las asignaciones.

---

## 3.2 Ineficiencia operativa

La planificación manual requiere tiempo para revisar:

- Disponibilidad de instructores.
- Ambientes disponibles.
- Fichas de formación.
- Bloques horarios.
- Posibles cruces.

La revisión manual puede generar reprocesos cuando aparece un conflicto después de completar una asignación.

---

## 3.3 Opacidad de datos

Cuando la información está distribuida, se dificulta contar con una única fuente de verdad.

Esto afecta la capacidad de consultar rápidamente el estado de:

- Ambientes.
- Instructores.
- Fichas.
- Horarios.
- Disponibilidad.

---

# 4. Objetivo de la solución

Desarrollar un sistema centralizado para la gestión de horarios académicos que permita organizar fichas, instructores, ambientes y bloques horarios, incorporando validaciones automáticas para prevenir conflictos antes de guardar una asignación.

## Objetivos específicos

- Centralizar la información académica relacionada con la programación.
- Facilitar la consulta de disponibilidad.
- Reducir los conflictos de horarios.
- Automatizar la validación de asignaciones.
- Mejorar la velocidad del proceso de planificación.
- Facilitar la consulta de horarios desde diferentes dispositivos.
- Mejorar la visibilidad sobre la utilización de ambientes.
- Mantener la información actualizada después de publicar cambios.

---

# 5. Actores del sistema

La solución contempla diferentes actores que participan en la gestión académica.

## 5.1 Coordinador Académico

### Responsabilidad

Planificar y organizar la programación académica.

### Necesidad principal

Realizar asignaciones de forma rápida evitando conflictos.

### Problema identificado

Cuando ocurre un cambio, puede ser necesario rehacer parte de la planificación.

### Solución propuesta

Una interfaz de orquestación visual con alertas preventivas antes de guardar una asignación.

---

## 5.2 Instructor

### Responsabilidad

Consultar y ejecutar las actividades académicas programadas.

### Necesidad principal

Conocer su disponibilidad y agenda exacta.

### Solución propuesta

Consulta en tiempo real de su horario y disponibilidad desde una interfaz adaptable a diferentes dispositivos.

---

## 5.3 Administrador de Ambientes

### Responsabilidad

Gestionar la infraestructura disponible para las actividades de formación.

### Necesidad principal

Conocer la ocupación de aulas, talleres y laboratorios.

### Solución propuesta

Información centralizada de ambientes y reportes para visualizar su utilización.

---

# 6. Modelo actual vs. modelo propuesto

## 6.1 Modelo actual — Gestión manual

- Información distribuida.
- Archivos locales o compartidos.
- Comunicación mediante diferentes medios.
- Prevención de errores basada principalmente en revisión humana.
- Cambios que pueden tardar en reflejarse.
- Posibilidad de reprocesos.
- Validación manual de disponibilidad.

## 6.2 Modelo propuesto — Gestión automatizada

- Plataforma web centralizada.
- Interfaz responsiva.
- Información consolidada.
- Validación automática de conflictos.
- Actualización de información después de publicar.
- Consulta de disponibilidad.
- Bloqueo de asignaciones inválidas.
- Mayor control sobre los recursos académicos.

---

# 7. Arquitectura de la solución

La solución se organiza en tres capas principales.

## 7.1 Capa de presentación / Frontend

Responsable de las interfaces utilizadas por los usuarios.

Características propuestas:

- Interfaces interactivas.
- Diseño responsivo.
- Visualización de calendarios.
- Formularios dinámicos.
- Navegación orientada a las necesidades de cada rol.

---

## 7.2 Capa de negocio / Backend

Representa el núcleo lógico del sistema.

Responsabilidades principales:

- Ejecutar las reglas de negocio.
- Gestionar la autenticación.
- Procesar las asignaciones.
- Ejecutar el motor de validación.
- Rechazar asignaciones inválidas.
- Gestionar la comunicación con la base de datos.

---

## 7.3 Capa de datos / Base de datos

Almacena de forma centralizada la información del sistema.

Debe mantener la relación e integridad entre:

- Fichas.
- Usuarios.
- Instructores.
- Ambientes.
- Bloques de horario.
- Asignaciones.

---

# 8. Flujo general del sistema

El flujo principal propuesto se divide en cinco etapas.

## Paso 1 — Autenticación segura

El usuario ingresa al sistema y, de acuerdo con su rol, se carga el dashboard correspondiente.

## Paso 2 — Selección de parámetros

El usuario selecciona la ficha de formación y el bloque de horario que desea gestionar.

## Paso 3 — Asignación de recursos

El sistema muestra los instructores y ambientes disponibles para el bloque seleccionado.

## Paso 4 — Validación automática

Antes de guardar, el backend comprueba las reglas correspondientes y verifica que no existan colisiones.

## Paso 5 — Publicación

Si la asignación es válida:

1. Se actualiza la base de datos.
2. Se registra la nueva programación.
3. El horario queda disponible para los usuarios correspondientes.

---

# 9. Módulos principales

El sistema está organizado alrededor de seis módulos integrados.

## 9.1 Fichas

Permite gestionar grupos de formación y relacionarlos con la programación académica.

## 9.2 Instructores

Permite administrar la información relacionada con el cuerpo docente, incluyendo sus datos académicos, especialidades y disponibilidad.

## 9.3 Ambientes

Permite gestionar aulas, talleres y laboratorios, incluyendo información como su capacidad.

## 9.4 Disponibilidad

Permite gestionar las franjas de disponibilidad de los instructores.

## 9.5 Asignaciones

Es el módulo donde se relacionan:

- Fichas.
- Instructores.
- Ambientes.
- Horarios.

## 9.6 Horarios

Permite consultar la programación mediante calendarios y vistas orientadas a cada usuario.

---

# 10. Historias de usuario

## HU-01 — Validar conflictos de ambiente

**Como Coordinador**, quiero que el sistema me alerte si intento asignar un ambiente ocupado, para evitar cruces de horarios.

### Criterios de aceptación

- El sistema debe verificar si el ambiente ya está reservado.
- La validación debe realizarse antes de guardar.
- El botón de guardar debe impedir la confirmación cuando exista un conflicto.
- El sistema debe mostrar el conflicto específico al usuario.

---

## HU-02 — Consultar horario del instructor

**Como Instructor**, quiero visualizar mi horario semanal en una vista de calendario, para planificar y consultar mis clases.

### Criterios de aceptación

- La vista debe mostrar las clases organizadas por día.
- Debe permitir identificar el ambiente.
- Debe permitir identificar la ficha.
- La interfaz debe adaptarse a diferentes dispositivos.

---

## HU-03 — Gestionar capacidad de ambientes

**Como Administrador**, quiero registrar la capacidad máxima de un ambiente, para evitar asignaciones que superen su capacidad.

### Criterios de aceptación

- La capacidad debe registrarse al crear o configurar un ambiente.
- El valor debe ser numérico.
- El sistema debe comparar la capacidad del ambiente con la cantidad de aprendices.
- Una asignación que supere la capacidad debe ser bloqueada.

---

# 11. Propuesta UX/UI

La interfaz debe estar orientada a reducir errores y facilitar la consulta de información.

## 11.1 Jerarquía visual

Se propone una navegación lateral minimalista para aprovechar mejor el espacio de trabajo.

Debe priorizar las funciones que cada rol utiliza con mayor frecuencia.

---

## 11.2 Alertas y feedback inmediato

El sistema debe informar inmediatamente el resultado de una acción.

### Estados propuestos

- **Verde:** operación exitosa.
- **Rojo:** error o conflicto.
- **Mensaje específico:** explicación del problema encontrado.

No basta con indicar que existe un error; el usuario debe conocer qué recurso genera el conflicto.

---

## 11.3 Selectores dinámicos

Los formularios deben mostrar únicamente opciones compatibles con los parámetros seleccionados.

Por ejemplo:

Si se selecciona un bloque horario específico, el sistema debe filtrar los ambientes disponibles para ese momento.

Esto reduce errores y evita que el usuario tenga que revisar manualmente opciones que no están disponibles.

---

## 11.4 Diseño responsivo

La interfaz debe adaptarse a diferentes tamaños de pantalla.

En dispositivos móviles, el calendario puede transformarse en una vista de agenda que facilite la consulta del instructor.

---

# 12. Motor de validación

El motor de validación constituye uno de los componentes principales de la solución.

Su función es verificar una asignación antes de permitir que sea guardada.

## Datos evaluados

La validación parte de la combinación:

`Ficha + Instructor + Ambiente + Día/Hora`

## Validación del instructor

El sistema debe comprobar:

- Si el instructor ya tiene otra clase en el mismo horario.
- Si el instructor se encuentra disponible en la franja seleccionada.

## Validación del ambiente

El sistema debe comprobar:

- Si el ambiente ya está reservado.
- Si existe otra ficha asignada al mismo ambiente en la misma fecha y hora.

## Validación de capacidad

El sistema debe comprobar:

- Cantidad de aprendices de la ficha.
- Capacidad máxima del ambiente.

Si la cantidad de aprendices supera la capacidad disponible, la asignación debe ser rechazada.

## Resultado

### Si existe conflicto

La transacción no debe completarse y el usuario debe recibir información sobre el conflicto.

### Si no existe conflicto

La asignación se considera válida y la información puede ser actualizada en la base de datos.

---

# 13. Indicadores y metas

La propuesta incluye indicadores para medir el impacto esperado del sistema.

> **Importante:** los valores de esta sección corresponden a metas o indicadores planteados en la presentación. No deben presentarse como resultados reales si todavía no se han obtenido mediante pruebas.

## 13.1 Reducción de conflictos

**Meta indicada:** 99.9% de reducción de conflictos de horario reportados en la primera semana de clases.

## 13.2 Reducción del tiempo de generación

**Meta indicada:** reducción del tiempo promedio para generar el horario de una ficha completa, planteada en la presentación como una disminución aproximada del 70%.

## 13.3 Optimización y visibilidad

**Meta indicada:** 85%+ de optimización y visibilidad del uso real de la infraestructura física.

## 13.4 Precisión en disponibilidad docente

El sistema busca respetar las franjas de contratación y disponibilidad de los instructores, evitando situaciones de sobrecarga.

---

# 14. Beneficios de la solución

## 14.1 Reducción de conflictos

La validación automática permite detectar incompatibilidades antes de confirmar una asignación.

## 14.2 Optimización de recursos

La información centralizada facilita conocer la disponibilidad y utilización de los ambientes.

## 14.3 Recuperación de tiempo administrativo

La automatización busca disminuir el tiempo dedicado a revisiones manuales y reprocesos.

## 14.4 Información centralizada

La plataforma busca funcionar como una fuente central de información para los actores involucrados.

## 14.5 Escalabilidad

La propuesta plantea una arquitectura preparada para ser utilizada en diferentes centros de formación.

## 14.6 Mejor experiencia de usuario

Las interfaces responsivas, los filtros dinámicos, los calendarios y las alertas inmediatas buscan facilitar la interacción con el sistema.

---

# 15. Conclusiones

El Sistema de Gestión de Horarios Académicos SENA propone transformar un proceso de planificación dependiente de revisiones manuales en un proceso centralizado y automatizado.

La principal propuesta de valor se encuentra en el **motor de validación**, que permite verificar las condiciones de una asignación antes de almacenarla.

La solución integra seis áreas principales:

- Fichas.
- Instructores.
- Ambientes.
- Disponibilidad.
- Asignaciones.
- Horarios.

A nivel de experiencia de usuario, se proponen interfaces responsivas, navegación organizada, alertas de feedback inmediato y filtros dinámicos que reduzcan la posibilidad de error.

En conjunto, la propuesta busca mejorar la gestión de horarios, reducir conflictos, aprovechar mejor los ambientes y facilitar el trabajo de coordinadores, instructores y administradores.

---

## Nota metodológica

Este documento conserva el contenido central de la presentación `MockUp.pptx` y lo reorganiza siguiendo el patrón estructural observado en los archivos `.md` más completos del grupo: introducción, análisis del problema, actores/roles, funcionamiento, arquitectura, módulos, historias de usuario, UX/UI, reglas de validación, indicadores y conclusiones.

No se incorporan como hechos resultados que no estén presentes en el material proporcionado. Los porcentajes se mantienen como **metas/indicadores planteados** en la presentación.

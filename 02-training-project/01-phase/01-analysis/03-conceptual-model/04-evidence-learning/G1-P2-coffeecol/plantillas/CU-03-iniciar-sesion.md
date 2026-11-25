# CU-03 · Iniciar sesión con Firebase

| Campo | Contenido |
|---|---|
| Identificador y nombre | CU-03 · Iniciar sesión con Firebase (incluye CU-17 Sincronizar usuario) |
| Requisitos que atiende | RF-023, RF-024, RF-027, RF-028 (RNF-010) |
| Actor primario / secundarios | Visitante / Firebase Authentication |
| Objetivo del actor | Acceder como cliente sin tener que recordar una contraseña |
| Precondiciones | El visitante tiene conexión a internet y una cuenta de Google o acceso a su correo |
| Disparador | El visitante pulsa «Iniciar sesión» |
| Flujo principal | 1. El visitante pulsa «Iniciar sesión».<br>2. El sistema muestra las opciones de acceso.<br>3. El visitante elige continuar con Google.<br>4. El sistema solicita la identidad al servicio externo.<br>5. El servicio externo pide al visitante el consentimiento de identidad.<br>6. El visitante aprueba el consentimiento.<br>7. El servicio externo valida la identidad y la devuelve al sistema.<br>8. El sistema registra o actualiza al usuario (CU-17).<br>9. El sistema abre la sesión y lleva al usuario al módulo que corresponde a su rol. |
| Flujos alternos | **A1.** (paso 3) Si el visitante elige el enlace mágico, ingresa su correo, el sistema envía un enlace de un solo uso, el visitante lo abre desde su correo y el caso continúa en el paso 7. |
| Excepciones | **E1.** (paso 6) Si el visitante cancela el consentimiento, el sistema permanece en la pantalla de acceso y el caso termina sin sesión.<br>**E2.** (paso 4) Si el servicio externo no responde, el sistema avisa el problema de forma amable y permite reintentar, sin afectar la navegación del catálogo. |
| Postcondiciones | Con éxito: el usuario queda autenticado, existe su registro de cliente actualizado y sus compras y puntos quedan ligados a su cuenta |
| Reglas de negocio | Los clientes no usan contraseña propia (Google o enlace mágico). El rol del usuario decide a qué módulo se le lleva. |
| Pantalla del prototipo | [pantalla-2-iniciar-sesion](../prototipo/pantalla-2-iniciar-sesion.png) |
| Diagrama de actividades | [actividad-iniciar-sesion](../diagramas/actividad-iniciar-sesion.png) |

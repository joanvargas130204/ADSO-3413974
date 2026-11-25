# CU-11 · Gestionar productos

| Campo | Contenido |
|---|---|
| Identificador y nombre | CU-11 · Gestionar productos (se extiende con CU-25 Cargar imagen de producto) |
| Requisitos que atiende | RF-045, RF-046, RF-047 (RNF-005) |
| Actor primario / secundarios | Administrador / ninguno |
| Objetivo del actor | Mantener actualizado el catálogo que ven los clientes |
| Precondiciones | El administrador inició sesión |
| Disparador | El administrador abre la sección de productos del panel |
| Flujo principal (crear producto) | 1. El administrador abre la sección de productos.<br>2. El sistema muestra el inventario con la posibilidad de buscar, ordenar y filtrar.<br>3. El administrador elige crear un producto.<br>4. El sistema solicita nombre, descripción, precio, categoría y stock.<br>5. El administrador diligencia los datos.<br>6. El administrador confirma.<br>7. El sistema comprueba que los datos obligatorios estén completos y que el precio y el stock sean válidos.<br>8. El sistema registra el producto y lo publica en el catálogo.<br>9. El sistema actualiza el inventario mostrado. |
| Flujos alternos | **A1.** (paso 3) Si el administrador busca, ordena o filtra el inventario (RF-047), el sistema muestra el resultado y el caso continúa en el paso 3.<br>**A2.** (paso 3) Si el administrador elige retirar un producto, el sistema pide confirmación; al confirmarla, lo retira del catálogo activo y actualiza el inventario; el caso termina con éxito.<br>**A3.** (paso 5, punto de extensión «adjuntar imagen») Si el administrador desea asociar una imagen, se ejecuta CU-25 Cargar imagen de producto y el caso continúa en el paso 6. |
| Excepciones | **E1.** (paso 7) Si faltan datos obligatorios o el precio o el stock no son válidos, el sistema señala los campos y regresa al paso 5 sin registrar nada.<br>**E2.** (paso 1) Si la sesión del administrador venció o no es válida, el sistema rechaza la solicitud y lo lleva a iniciar sesión.<br>**E3.** (A3) Si la imagen no es válida (CU-26), el sistema la rechaza y el producto puede guardarse sin imagen o con otra. |
| Postcondiciones | El catálogo refleja el producto creado o retirado para todos los visitantes |
| Reglas de negocio | Solo el administrador con sesión válida puede cambiar el catálogo. Un producto retirado deja de mostrarse pero no se pierde el historial de pedidos que lo incluyen. |
| Pantalla del prototipo | [pantalla-3-gestionar-productos](../prototipo/pantalla-3-gestionar-productos.png) |

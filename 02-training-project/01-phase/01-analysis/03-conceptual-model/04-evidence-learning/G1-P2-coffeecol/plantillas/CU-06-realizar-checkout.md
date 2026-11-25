# CU-06 · Realizar checkout y generar pedido

| Campo | Contenido |
|---|---|
| Identificador y nombre | CU-06 · Realizar checkout y generar pedido (incluye CU-19 Validar datos de entrega y CU-20 Acumular puntos por compra) |
| Requisitos que atiende | RF-017, RF-018, RF-019, RF-020, RF-021, RF-038 (RNF-006, RNF-009, RNF-016, RNF-017) |
| Actor primario / secundarios | Cliente registrado / ninguno |
| Objetivo del actor | Recibir en su domicilio los productos de su carrito y obtener un número de pedido |
| Precondiciones | El cliente inició sesión y su carrito tiene al menos un producto |
| Disparador | El cliente abre el checkout desde el carrito |
| Flujo principal | 1. El cliente abre el checkout desde el carrito.<br>2. El sistema precarga los datos de entrega guardados del cliente.<br>3. El cliente confirma dirección, teléfono y municipio de entrega.<br>4. El sistema valida los datos de entrega (CU-19).<br>5. El cliente acepta la política de tratamiento de datos personales.<br>6. El sistema muestra el resumen con el total recalculado y el costo de despacho desglosado.<br>7. El cliente revisa el resumen y confirma el pedido.<br>8. El sistema verifica que haya existencias de todos los productos.<br>9. El sistema registra el pedido en estado pendiente y acredita los puntos de la compra (CU-20).<br>10. El sistema muestra el número del pedido y vacía el carrito. |
| Flujos alternos | **A1.** (paso 2) Si el cliente no tiene direcciones guardadas, el sistema no precarga datos y el cliente los diligencia; el caso continúa en el paso 3. |
| Excepciones | **E1.** (paso 4) Si algún dato es inválido o está vacío, el sistema resalta los campos con error y regresa al paso 3.<br>**E2.** (paso 5) Si el cliente no acepta la política de datos, el sistema informa que es obligatoria y el caso termina sin pedido.<br>**E3.** (paso 8) Si algún producto está agotado, el sistema informa cuáles y el caso termina sin pedido.<br>**E4.** (paso 9) Si el registro falla, el sistema deshace la operación, informa el error y no se crea el pedido ni se acreditan puntos. |
| Postcondiciones | Existe un pedido en estado pendiente ligado al cliente y a su dirección de entrega, con su código único; los puntos quedaron acreditados; el carrito quedó vacío |
| Reglas de negocio | El total siempre se recalcula con los precios vigentes. El despacho cuesta $12.000 COP y es gratis si el subtotal supera $150.000 COP. Se acredita 1 punto por cada $1.000 COP. El pedido y los puntos se registran juntos o no se registra ninguno. El resumen detalla productos, despacho y total. No hay cobro en línea. |
| Pantalla del prototipo | [pantalla-1-realizar-checkout](../prototipo/pantalla-1-realizar-checkout.png) |
| Diagrama de actividades | [actividad-realizar-checkout](../diagramas/actividad-realizar-checkout.png) |

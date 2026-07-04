# user-stories

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Historias de usuario derivadas de los casos de uso principales del SRS (sección 9: CU01, CU02, CU03).

## Contenido

### HU01 — Registrar Venta (CU01)

**Como** empleado o administrador del supermercado,
**quiero** registrar una venta seleccionando productos del catálogo,
**para** cobrar sin calculadora en menos de 145 segundos.

**Flujo normal:**

1. El operario inicia una nueva venta y busca productos por nombre.
2. El sistema muestra precio y stock, y calcula el subtotal en tiempo real.
3. El operario selecciona el método de pago. Si es efectivo, ingresa el monto recibido; el sistema calcula el cambio.
4. El operario confirma la venta. El sistema descuenta el stock, genera el tiquete y vuelve al POS.

**Criterios de aceptación / excepciones:**

- Si el producto no se encuentra, el sistema notifica al Administrador para agregarlo y la venta permanece abierta.
- Si el stock es cero, el sistema bloquea el ítem e informa al operario.
- Si cae la conexión, el sistema activa el modo offline automáticamente (RNF02).

**Requisitos relacionados:** RF01, RF03, RF06, RNF01, RNF02, RNF03.

### HU02 — Gestionar Catálogo (CU02)

**Como** Carlos Ruiz (Administrador),
**quiero** crear, editar o eliminar productos del catálogo,
**para** mantener precios y stock actualizados en máximo 3 clics, sin soporte técnico.

**Flujo normal:**

1. El Administrador accede al módulo Catálogo y selecciona Nuevo / Editar / Eliminar.
2. Completa el formulario (nombre, precio, categoría, stock, mínimo) y guarda.
3. El sistema valida los datos, guarda y actualiza el POS en tiempo real para todos los empleados.

**Criterios de aceptación / excepciones:**

- Nombre duplicado: el sistema ofrece ver el producto existente o cambiar el nombre.
- Precio inválido: el campo se marca en rojo y no se guarda hasta corregir.
- Límite de 90 productos: el botón "Nuevo" se deshabilita con mensaje explicativo.

**Requisitos relacionados:** RF02, RNF01, RNF06, RN02.

### HU03 — Corte de Caja Diario (CU03)

**Como** Carlos Ruiz (Administrador),
**quiero** cerrar la jornada con un resumen digital trazable,
**para** detectar diferencias entre el efectivo físico y lo registrado por el sistema.

**Flujo normal:**

1. El Administrador accede al módulo Corte de Caja al final del día.
2. El sistema muestra: nº de transacciones, total efectivo, total digital y desglose por empleado.
3. El Administrador ingresa el efectivo físico contado; el sistema calcula la diferencia (🟢/🟡/🔴).
4. El Administrador confirma el cierre; el sistema registra, activa el backup y genera el reporte en PDF.

**Criterios de aceptación / excepciones:**

- Diferencia mayor a $5.000 COP: alerta roja con opción de revisar el historial antes de confirmar.
- Corte ya realizado: el sistema permite ver el reporte o ejecutar un corte de corrección.

**Requisitos relacionados:** RF04, RNF08, RN02.

## Referencias

- [04-requirements/functional.md](./functional.md)
- [04-requirements/traceability-matrix.md](./traceability-matrix.md)
- [02-domain/domain-events.md](../02-domain/domain-events.md)

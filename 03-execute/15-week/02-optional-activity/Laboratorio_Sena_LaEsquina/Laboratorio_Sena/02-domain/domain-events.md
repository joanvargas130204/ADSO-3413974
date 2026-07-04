# domain-events

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Eventos de dominio relevantes, derivados de los flujos normales y excepciones de los casos de uso CU01–CU03 del SRS.

## Contenido

| Evento | Disparado por | Efecto / significado funcional |
|--------|---------------|----------------------------------|
| VentaRegistrada | Operario confirma una venta (CU01) | Descuenta stock, genera tiquete, vuelve al POS |
| StockAgotado | Stock de un producto llega a 0 (CU01) | Bloquea el ítem en el POS e informa al operario |
| StockMinimoAlcanzado | Stock de un producto llega a su mínimo (RF03) | Genera alerta visible para el Administrador |
| ProductoNoEncontrado | Operario busca un producto inexistente (CU01) | Notifica al Administrador para agregarlo; la venta permanece abierta |
| ModoOfflineActivado | Se detecta caída de conexión durante una venta (CU01, RNF02) | El sistema continúa operando localmente y sincroniza al recuperar conexión |
| ProductoCreado / ProductoActualizado / ProductoEliminado | Administrador gestiona el catálogo (CU02) | Actualiza el POS en tiempo real para todos los empleados |
| LimiteDeCatalogoAlcanzado | Catálogo llega a 90 productos (CU02) | Deshabilita el botón "Nuevo" con mensaje explicativo |
| CorteDeCajaRealizado | Administrador confirma el cierre de caja (CU03) | Registra el corte, activa backup y genera reporte en PDF |
| DiferenciaDeCajaDetectada | Diferencia entre caja física y sistema > $5.000 (CU03) | Alerta roja con opción de revisar historial antes de confirmar |
| AbonoRegistrado | Cliente realiza un pago parcial sobre un Fiado (RF05) | Actualiza el saldo pendiente |
| FiadoVencido | Un Fiado supera 30 días sin abono (RF05) | Genera alerta de vencimiento |

## Referencias

- [04-requirements/user-stories.md](../04-requirements/user-stories.md)
- [02-domain/entities-and-rules.md](./entities-and-rules.md)

# domain-map

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

El dominio del Supermercado La Esquina se organiza alrededor de seis contextos, derivados directamente de los módulos del MVP definidos en el SRS (sección 4 — Alcance).

## Contenido

| Contexto / Bounded Context | Módulo SRS | Responsabilidad |
|------------------------------|-------------|------------------|
| Catálogo | M1 — Inventario / Catálogo | Productos, categorías, stock y stock mínimo |
| Ventas | M2 — Ventas / POS | Registro de ventas, cálculo de total, método de pago |
| Identidad y Acceso | M3 — Usuarios y Roles | Administrador y Empleado, permisos diferenciados |
| Caja | M4 — Corte de Caja | Resumen diario, diferencia vs. caja física, historial |
| Comprobantes | M5 — Tiquetes | Generación de tiquete (impreso o PDF/WhatsApp) |
| Cartera (Fiado) | M6 — Gestión de Fiado | Créditos por cliente, abonos, saldo, alertas de vencimiento |

### Relaciones entre contextos

- **Ventas** descuenta stock en **Catálogo** al confirmar una venta (RF03).
- **Ventas** puede originar un crédito en **Cartera (Fiado)** cuando el cliente no paga de inmediato (RF05).
- **Ventas** alimenta a **Caja** para el corte diario (RF04) y a **Comprobantes** para emitir el tiquete (RF06).
- **Identidad y Acceso** acota lo que cada rol puede ver o modificar en los demás contextos (RNF04).

## Referencias

- [01-context/scope.md](../01-context/scope.md)
- [04-requirements/functional.md](../04-requirements/functional.md)
- [02-domain/entities-and-rules.md](./entities-and-rules.md)
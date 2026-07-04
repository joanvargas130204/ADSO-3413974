# Glosario

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

| Término | Definición | Contexto |
|---------|------------|----------|
| POS (Punto de Venta) | Módulo donde el operario selecciona productos, calcula el total y registra el método de pago de una venta | Dominio |
| SKU / Producto | Ítem del catálogo con nombre, precio, categoría, stock y stock mínimo | Dominio |
| Stock mínimo | Cantidad de un producto bajo la cual el sistema genera una alerta al Administrador | Dominio |
| Fiado | Crédito informal otorgado a un cliente, registrado con monto, fecha, abonos y saldo pendiente | Dominio |
| Abono | Pago parcial que un cliente realiza sobre un saldo de fiado | Dominio |
| Corte de Caja | Resumen diario de ventas por método de pago, comparado contra el efectivo físico contado | Dominio |
| Diferencia de caja | Resultado de comparar el total calculado por el sistema contra el efectivo físico contado al cierre; se clasifica en 🟢/🟡/🔴 según el monto | Dominio |
| Tiquete | Comprobante de venta (impreso o PDF/WhatsApp) con fecha, productos, total y cajero | Dominio |
| Modo offline | Capacidad del sistema de operar con plena funcionalidad sin conexión a internet, sincronizando al recuperar conexión | Sistema |
| MoSCoW | Técnica de priorización de requisitos: Must have, Should have, Could have, Won't have | Sistema |
| Administrador | Rol con acceso total al sistema (Carlos Ruiz) | Sistema |
| Empleado | Rol con acceso a ventas e inventario en modo lectura, sin ver reportes financieros | Sistema |
| RF | Requisito Funcional | Sistema |
| RNF | Requisito No Funcional | Sistema |
| RN | Requisito de Negocio | Sistema |
| CU | Caso de Uso | Sistema |
| MVP | Producto Mínimo Viable | Sistema |

## Referencias

- [04-requirements/functional.md](../04-requirements/functional.md)
- [02-domain/entities-and-rules.md](../02-domain/entities-and-rules.md)

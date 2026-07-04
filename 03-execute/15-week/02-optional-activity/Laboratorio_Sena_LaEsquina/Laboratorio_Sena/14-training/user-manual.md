# user-manual

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## Contexto

Manual para los empleados (Martha Suárez, Julián Torres, Diego Morales) y para el Administrador en su rol de cajero, basado en CU01 — Registrar Venta. Meta: completar una venta tras máximo 2 horas de inducción (RNF01).

## Contenido

### Cómo registrar una venta

1. Inicia una nueva venta en la pantalla POS.
2. Busca cada producto por nombre. El sistema muestra precio y stock disponibles.
3. El subtotal se calcula automáticamente a medida que agregas productos.
4. Selecciona el método de pago:
   - **Efectivo:** ingresa el monto recibido; el sistema calcula el cambio.
   - **Digital:** selecciona el método; el sistema solo registra el dato, no procesa el pago.
5. Confirma la venta. El sistema descuenta el stock y genera el tiquete (impreso o PDF/WhatsApp).

### Qué hacer si...

| Situación | Qué hacer |
|-----------|-----------|
| El producto no aparece en la búsqueda | El sistema notifica al Administrador para que lo agregue; la venta queda abierta, puedes seguir con los demás productos |
| El producto muestra stock cero | El sistema bloquea ese ítem; informa al cliente y continúa con el resto de la venta |
| Se cae la conexión a internet | El sistema sigue funcionando en modo offline; sincronizará automáticamente al recuperar conexión |

### Tu historial de ventas (RF07)

Puedes consultar tus propias ventas filtradas por fecha o producto. No puedes ver las ventas de otros empleados ni los reportes financieros del negocio.

## Referencias

- [04-requirements/user-stories.md](../04-requirements/user-stories.md)
- [12-ux-ui/wireframes.md](../12-ux-ui/wireframes.md)

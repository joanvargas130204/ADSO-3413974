# Alcance

> Estado: 🟡 En progreso | Última actualización: 2026-06-20
> Autor: Por definir | Equipo: Análisis y Desarrollo de Software (SENA)

## En alcance

MVP de **POS + Inventario** organizado en 6 módulos:

| Módulo | Nombre | Alcance |
|--------|--------|---------|
| M1 | Inventario / Catálogo | Hasta 90 productos (nombre, precio, categoría, stock). Alertas de mínimo. |
| M2 | Ventas / POS | Selección de productos, cálculo automático del total, registro de método de pago. |
| M3 | Usuarios y Roles | Administrador (acceso total) · Empleado (ventas + inventario en lectura). |
| M4 | Corte de Caja | Resumen diario por método de pago, diferencia vs. caja física, historial. |
| M5 | Tiquetes | Generación de tiquete impreso o PDF/WhatsApp. |
| M6 | Gestión de Fiado | Créditos por cliente, abonos, saldo pendiente, alertas de vencimiento. |

## Fuera de alcance

- Integración automática con pasarelas de pago (Nequi, Daviplata, datáfono). El sistema **registra** el método de pago pero **no procesa** la transacción digital.
- Facturación electrónica DIAN.
- Gestión contable / declaración de impuestos.
- App o portal para clientes finales.
- Integración con sistemas de proveedores.
- Múltiples sucursales (contemplada como escalabilidad futura, ver [RNF07](../04-requirements/non-functional.md)).

## Supuestos

- El propietario (Carlos Ruiz) es el único administrador del sistema durante el MVP.
- El catálogo no supera los 90 productos durante el MVP (ver [RF02](../04-requirements/functional.md) y límite descrito en [CU02](../04-requirements/user-stories.md)).
- El negocio cuenta con hardware de bajo costo (Android 8.0/2 GB RAM o Windows 10/2 GB RAM), sin hardware especializado (RNF05).
- La conexión a internet es intermitente; el sistema debe operar en modo offline (RNF02).

## Restricciones

- Sin licencia mensual: costo único o licencia anual asequible, sin suscripciones recurrentes de alto costo (RN01).
- Autonomía operativa: Carlos Ruiz debe poder reiniciar, actualizar precios y cerrar caja sin asistencia técnica externa (RN02).
- Curva de aprendizaje máxima de 2 horas para usuarios sin experiencia técnica (RNF01).
- UI en español colombiano.

## Referencias

- [04-requirements/functional.md](../04-requirements/functional.md)
- [04-requirements/non-functional.md](../04-requirements/non-functional.md)

